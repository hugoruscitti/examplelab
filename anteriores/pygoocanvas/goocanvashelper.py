import gobject
gobject.threads_init()
import goocanvas
import gtk
 
## GTK Conveinence Functions
 
def widget_helper(klass, func=None, *args, **kwargs):
    """Used to create convenience functions like scrolled"""
    def retfunc(*children):
        ret = klass(*args, **kwargs)
        for child in children:
            if func:
                func(ret, child)
            else:
                ret.add(child)
        return ret
    return retfunc
 
def container_helper(klass, *args, **kwargs):
    """Used to create convinience functions like HBox() and VBox()"""
    def childfunc(container, child):
        widget, end, expand, fill = child
        if end == 'end':
            container.pack_end(widget, expand, fill)
        elif end == 'start':
            container.pack_start(widget, expand, fill)
        else:
            container.add(widget)
    return widget_helper(klass, childfunc, *args, **kwargs)
 
scrolled = widget_helper(gtk.ScrolledWindow)
hbox = container_helper(gtk.HBox)
vbox = container_helper(gtk.VBox)
 
## GooCanvas Convenience Functions
 
class smartgroup(goocanvas.Group):
    """Extends goocanvas.Group() with the notion of position
    through gobject properties x, y"""
    __gtype_name__ = 'SmartGroup'
 
    x = gobject.property(type=int, default=0)
    y = gobject.property(type=int, default=0)
    width = gobject.property(type=int, default=0)
    height = gobject.property(type=int, default=0)
 
    def __init__(self, *args, **kwargs):
        goocanvas.Group.__init__(self, *args, **kwargs)
        self.children = {}
        self.connect("notify::x", self.move_x_children)
        self.connect("notify::y", self.move_y_children)
 
    def move_x_children(self, object, prop):
        for child, (x, y) in self.children.items():
            child.props.x = self.x + x
 
    def move_y_children(self, object, prop):
        for child, (x, y) in self.children.items():
            child.props.y = self.y + y
 
    def add_child(self, child, pos=(0,0)):
        goocanvas.Group.add_child(self, child)
        self.children[child] = pos
        #child.connect("notify::width", self.update_width)
        #child.connect("notify::height", self.update_height)
        #self.update_width()
 
def event_coords(canvas, event):
    """returns the coordinates of an event"""
    return canvas.convert_from_pixels(event.x, event.y)
 
def point_difference(p1, p2):
    """Returns the 2-dvector difference p1 - p2"""
    p1_x, p1_y = p1
    p2_x, p2_y = p2
    return (p1_x - p2_x, p1_y - p2_y)
 
def point_sum(p1, p2):
    """Returns the 2d vector sum p1 + p2"""
    p1_x, p1_y = p1
    p2_x, p2_y = p2
    return (p1_x + p2_x, p1_y + p2_y)
 
def point_mul(factor, point):
    """Returns a scalar multiple factor * point"""
    return tuple(factor * v for v in point)
 
def pos(item):
    """Returns a tuple x, y representing the position of the 
    supplied goocanvas Item"""
    return item.props.x, item.props.y
 
def pos_change(item, callback):
    """Connects the callback to the x and y property notificaitons.
    Do not call this function again without calling unlink_pos_change()
    first"""
    item.set_data("x_sig_hdl", item.connect("notify::x", callback))
    item.set_data("y_sig_hdl", item.connect("notify::y", callback))
 
def unlink_pos_change(item):
    """Disconnects signal handlers after calling pos_change()"""
    item.disconnect(item.get_data("x_sig_hdl"))
    item.disconnect(item.get_data("y_sig_hdl"))
 
def size(item):
    """Returns the tuple (<width>, <height>) of item"""
    return item.props.width, item.props.height
 
def set_size(item, size):
    """Sets the size of the item given size, a tuple of 
    (<width>, <height>)"""
    item.props.width, item.props.height = size
 
def top(item):
    return item.props.y
 
def bottom(item):
    return item.props.y + item.props.height
 
def left(item):
    return item.props.x
 
def right(item):
    return item.props.x + item.props.width
 
def top_right(item):
    return (right(item), top(item))
 
def bottom_right(item):
    return point_sum(pos(item), size(item))
 
def set_pos(item, pos):
    """Sets the position of item given pos, a tuple of (<x>, <y>)"""
    item.props.x, item.props.y = pos
 
def width(item):
    return item.props.width
 
def height(item):
    return item.props.height
 
def center(item):
    return point_sum(pos(item), point_mul(0.5, size(item)))
 
# these are callbacks for implementing "dragable object features
def drag_start(item, target, event, canvas):
    """A callback which starts the drag operation of a dragable 
    object"""
    item.set_data("dragging", True)
    item.set_data("pendown", point_difference(pos(item), 
        event_coords(canvas, event)))
    return True
 
def drag_end(item, target, event):
    """A callback which ends the drag operation of a dragable object"""
    item.set_data("dragging", False)
    return True
 
def translate_item_group(item, target, event, canvas, transform):
    """A callback which handles updating the position during a drag
    operation"""
    if item.get_data("dragging"):
        pos = point_sum(item.get_data("pendown"), event_coords(canvas, event))
        if transform:
            set_pos(item, transform(pos))
            return True
        set_pos(item, pos)
        return True
    return False
 
# callbacks for this feature are not implemented as nested 
# functions in order to minimize the potential memory impact this 
# might have when large numbers of dragable objects are present.
 
def make_dragable(canvas, item, transform=None):
    """Make item dragable with respect to the canvas. Call this 
    after make_selectable, or it will prevent the latter from working.
    """
    item.set_data("dragging", False)
    item.connect("button_press_event", drag_start, canvas)
    item.connect("button_release_event", drag_end)
    item.connect("motion_notify_event", translate_item_group, canvas,
        transform)
 
def group(*items):
    """Wrap all the canvas items in items in a smartgroup and return the
    resulting smartgroup. The item's current position is the offset
    within the smartgroup"""
    ret = smartgroup()
 
    for item in items:
        ret.add_child(item, pos(item))
 
    return ret
 
def make_item(factory):
    """Create a new goocanvas item given factory, a tuple of 
    * <class> - the class to create
    * <properties> - initial properties to set, such as color
    * <data> - initial data to set
    """
    klass, properties, data = factory
    ret = klass(**properties)
    for key, value in data.items():
        ret.set_data(key, value)
    return ret
 
def normalize_rect(mouse_down, cur_pos):
    """Given two points, representing the upper left and bottom right 
    corners of a rectangle (the order is irrelevant), return the tuple
    ((x,y), (width, height))"""
    w, h = point_difference(cur_pos, mouse_down)
    x, y = mouse_down
 
    if w < 0:
        w = abs(w)
        x -= w
    if h < 0:
        h = abs(h)
        y -= h
 
    return (x, y), (w, h)
 
def object_select_cb(item, target, event, canvas, changed_cb):
    prev = canvas.get_data("selected_objects")
    if (event.state & gtk.gdk.SHIFT_MASK):
        prev.add(item)
        changed_cb(prev, set())
    else:
        selected = set()
        selected.add(item)
        canvas.set_data("selected_objects", selected)
        changed_cb(selected, prev)
    return False
 
def make_selectable(canvas, object):
    """Make the object selectable with respect to canvas. This means
    that the item will be included in the current selection, and that
    clicking the object will select it. Must be called before 
    make_dragable, as it will block the action of this handler"""
    object.set_data("selectable", True)
    object.connect("button_press_event", object_select_cb, canvas,
        canvas.get_data("selection_callback"))
 
def manage_selection(canvas, marquee, overlap, changed_cb=None):
    """Keep track of the current selection in canvas, including
    * providing a rectangular selection marquee
    * tracking specific canvas objects
    Note: objects must be made selectable by calling make_selectable()
    on the object before they will be reported by any selection changes
    - overlap: True if you want items that merely intersect the 
        data field to be considered selected.
    - marquee: a goocanvas.Rectangle() to be used as the selection 
        marquee (really, any canvas item with x, y, width, height 
        properties). This object should not already be added to the
        canvas.
    - changed_cb: a callback with signature (selected, deselected)
      """
 
    def objects_under_marquee(event):
        pos, size = normalize_rect(mouse_down[0], event_coords(
            canvas, event))
        bounds = goocanvas.Bounds(*(pos + point_sum(pos, size)))
        selected = canvas.get_items_in_area(bounds, True, overlap, 
            containers)
        if selected:
            return set((found for found in selected if 
                found.get_data("selectable")))
        return set()
 
    def selection_start(item, target, event):
        root.add_child(marquee)
        cursor = event_coords(canvas, event)
        set_pos(marquee, cursor)
        selecting[0] = True
        mouse_down[0] = cursor
        set_pos(marquee, cursor) 
        set_size(marquee, (0, 0))
        return True
 
    def selection_end(item, target, event):
        selecting[0] = False
        marquee.remove()
        prev = canvas.get_data("selected_objects")
        selected = objects_under_marquee(event)
        canvas.set_data("selected_objects", selected)
        if changed_cb:
            changed_cb(selected, prev.difference(selected))
        return True
 
    def selection_drag(item, target, event):
        if selecting[0]:
            pos_, size_ = normalize_rect(mouse_down[0], 
                event_coords(canvas, event))
            set_size(marquee, size_)
            set_pos(marquee, pos_)
            return True
        return False
 
    canvas.set_data("selected_objects", set())
    canvas.set_data("selection_callback", changed_cb)
    containers = True
    selecting = [False]
    mouse_down = [None]
    root = canvas.get_root_item()
    root.connect("button_press_event", selection_start)
    root.connect("button_release_event", selection_end)
    root.connect("motion_notify_event", selection_drag)
