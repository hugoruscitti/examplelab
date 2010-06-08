import gtk
import cairo

class shapedWindow(gtk.DrawingArea):
        def __init__(self):
                gtk.DrawingArea.__init__(self)
                self.__pixbuf =  gtk.gdk.pixbuf_new_from_file('./logo.png')
                self.connect('size-allocate',self.size_allocated)
                self.connect('expose-event',self.do_expose_event)
                self.set_size_request(self.__pixbuf.get_width(),
                                self.__pixbuf.get_height())
       
        def size_allocated(self,win,allocation):
                w,h = (allocation.width, allocation.height)
                self.bitmap = gtk.gdk.Pixmap(None,w,h,1)
                context = self.bitmap.cairo_create()
               

                self.do_expose_event(self,'',context)
                parent = self.get_parent()
                win.shape_combine_mask(self.bitmap,0,0)
                parent.shape_combine_mask(self.bitmap,0,0)
               
        def do_expose_event(self, widget, event,allocate = False):
                if allocate:
                        context = allocate
                else:
                        context = self.window.cairo_create()
                if allocate:
                        context.set_operator(cairo.OPERATOR_DEST_OUT)
                        w,h = (self.allocation.width, self.allocation.height)
                        context.rectangle(0,0,w,h)
                        context.set_source_rgb(1,1,1)
                        context.paint()
                context.move_to(0,0)
                context.set_operator(cairo.OPERATOR_OVER)
                if allocate:
                        pixmap,mask = self.__pixbuf.render_pixmap_and_mask()
                        context.set_source_pixmap(mask,0,0)
                else:
                        context.set_source_pixbuf(self.__pixbuf,0,0)
                context.paint()
       

if __name__ == '__main__':
        window = gtk.Window()
        window.set_decorated(False)
        a = shapedWindow()
        window.add(a)
        window.show_all()
        gtk.main() 
