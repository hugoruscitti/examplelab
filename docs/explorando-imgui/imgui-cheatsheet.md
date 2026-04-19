# ImGui Cheatsheet

Referencia rápida de componentes y funciones de Dear ImGui.

## Inicialización

```javascript
// Inicialización básica
await ImGui.default();
ImGui.CreateContext();
ImGui_Impl.Init(ctx);
ImGui.StyleColorsDark();  // o StyleColorsLight()

// En el loop
ImGui_Impl.NewFrame(time);
ImGui.NewFrame();

// Al finalizar
ImGui.EndFrame();
ImGui.Render();
ImGui_Impl.RenderDrawData(ImGui.GetDrawData());
```

## Windows

```javascript
// Ventana básica
ImGui.Begin("Título de ventana");  // returns boolean (false = cerrada)
    // contenido...
ImGui.End();

// Ventana con flags
ImGui.Begin("Título", flags);
ImGui.Begin("Título", () => false, flags);  // con callback de cierre

// Window Flags
ImGui.WindowFlags.NoTitleBar
ImGui.WindowFlags.NoResize
ImGui.WindowFlags.NoMove
ImGui.WindowFlags.NoScrollbar
ImGui.WindowFlags.NoCollapse
ImGui.WindowFlags.AlwaysAutoResize
ImGui.WindowFlags.NoBackground
ImGui.WindowFlags.NoSavedSettings
ImGui.WindowFlags.MenuBar
```

## Widgets Básicos

```javascript
// Texto
ImGui.Text("Texto simple");
ImGui.TextColored(color, "Texto colored");  // color: {r, g, b, a}
ImGui.TextDisabled("Texto deshabilitado");
ImGui.TextWrapped("Texto con wrap");

// Label
ImGui.LabelText("label", "valor");
ImGui.TextUnformatted("sin formatting");  // más performante

// Botón
ImGui.Button("Click me");  // returns true cuando click
ImGui.SmallButton("small");  // botón pequeño
ImGui.InvisibleButton("id", width, height);  // área clickeable personalizada

// Checkbox
ImGui.Checkbox("label", value_ref);  // value_ref es función getter/setter
ImGui.CheckboxFlags("label", flags_ref, flags_value);

// Radio button
ImGui.RadioButton("label", active_ref);  // returns true cuando seleccionado
ImGui.RadioButton("label", value, valor_esperado);  // settea value cuando click
```

## Sliders y Drag

```javascript
// Slider
ImGui.SliderFloat("label", value_ref, min, max);
ImGui.SliderFloat2("label", values_ref, min, max);
ImGui.SliderFloat3("label", values_ref, min, max);
ImGui.SliderFloat4("label", values_ref, min, max);
ImGui.SliderInt("label", value_ref, min, max);
ImGui.SliderInt2("label", values_ref, min, max);
ImGui.SliderInt3("label", values_ref, min, max);
ImGui.SliderAngle("label", value_ref_rad, min_deg, max_deg);
ImGui.SliderScalar("label", data_type, value_ref, min, max);

// Drag (similar a slider pero con mouse drag)
ImGui.DragFloat("label", value_ref, speed, min, max);
ImGui.DragFloat2("label", values_ref, speed, min, max);
ImGui.DragFloat3("label", values_ref, speed, min, max);
ImGui.DragFloat4("label", values_ref, speed, min, max);
ImGui.DragInt("label", value_ref, speed, min, max);

// Input de texto
ImGui.InputText("label", text_ref);
ImGui.InputTextMultiline("label", text_ref, width, height);
ImGui.InputTextWithHint("label", "hint", text_ref);
ImGui.InputFloat("label", value_ref, step, step_fast);
ImGui.InputFloat2("label", values_ref, format, flags);
ImGui.InputFloat3("label", values_ref, format, flags);
ImGui.InputFloat4("label", values_ref, format, flags);
ImGui.InputInt("label", value_ref, step, step_fast);
ImGui.InputInt2("label", values_ref, flags);
ImGui.InputInt3("label", values_ref, flags);
ImGui.InputInt4("label", values_ref, flags);

// InputText Flags
ImGui.InputTextFlags.EnterReturnsTrue
ImGui.InputTextFlags.CallbackCompletion
ImGui.InputTextFlags.CallbackHistory
ImGui.InputTextFlags.ReadOnly
ImGui.InputTextFlags.Password
ImGui.InputTextFlags.Multiline
```

## Color Pickers

```javascript
// Color Picker
ImGui.ColorPicker3("label", color_ref);  // RGB
ImGui.ColorPicker4("label", color_ref);  // RGBA

// Color Edit
ImGui.ColorEdit3("label", color_ref);
ImGui.ColorEdit4("label", color_ref);

// Flags para color picker
ImGui.ColorEditFlags.NoAlpha
ImGui.ColorEditFlags.NoPicker
ImGui.ColorEditFlags.NoOptions
ImGui.ColorEditFlags.NoSmallPreview
ImGui.ColorEditFlags.NoInputs
ImGui.ColorEditFlags.NoTooltip
ImGui.ColorEditFlags.RGB
ImGui.ColorEditFlags.HSV
ImGui.ColorEditFlags.Uint8
```

## Trees y Collapse

```javascript
// Tree Node (colapsable)
ImGui.TreeNode("label");  // returns true si abierto
ImGui.TreeNode("id", "label con formato %s", arg);
ImGui.TreePush("id");  // push manual
    // contenido
ImGui.TreePop();  // pop manual
ImGui.Indent();  // sangría
ImGui.Unindent();  // remover sangría

// TreeNode Flags
ImGui.TreeNodeFlags.DefaultOpen
ImGui.TreeNodeFlags.OpenOnDoubleClick
ImGui.TreeNodeFlags.OpenOnArrow
ImGui.TreeNodeFlags.Leaf
ImGui.TreeNodeFlags.Bullet
ImGui.TreeNodeFlags.FramePadding
ImGui.TreeNodeFlags.CollapsingHeader
```

## Selectables

```javascript
// Selectable (clickeable highlight)
ImGui.Selectable("label");  // returns true si seleccionado
ImGui.Selectable("label", selected_ref);  //two-way binding
ImGui.Selectable("label", selected_ref, flags, size);

// SelectableFlags
ImGui.SelectableFlags.AllowDoubleClick
ImGui.SelectableFlags.DontClosePopups
ImGui.SelectableFlags.SpanAllColumns
```

## Combo y Dropdown

```javascript
// Combo
ImGui.Combo("label", current_item_ref, items_array);
ImGui.Combo("label", current_item_ref, "item1\nitem2\nitem3");
ImGui.Combo("label", current_item_ref, getter_fn, user_data, count);

// Combo con lambda getter
ImGui.Combo("label", current_idx, (idx) => items[idx], null, items.length);

// BeginCombo (manera avanzada)
ImGui.BeginCombo("label", preview_value);
    ImGui.Selectable("item 1", selected);
    ImGui.Selectable("item 2", selected);
ImGui.EndCombo();

// ComboFlags
ImGui.ComboFlags.PopupAlignLeft
ImGui.ComboFlags.HeightSmall
ImGui.ComboFlags.HeightRegular
ImGui.ComboFlags.HeightLarge
ImGui.ComboFlags.HeightLargest
ImGui.ComboFlags.NoArrowButton
ImGui.ComboFlags.NoPreview
```

## Lists

```javascript
// ListBox
ImGui.ListBox("label", current_item_ref, items_array, height);
ImGui.ListBox("label", current_item_ref, getter_fn, user_data, count);

// BeginListBox (manera avanzada)
ImGui.BeginListBox("label", size);  // size: {w, h} o null para auto
    ImGui.Selectable("item", selected);
ImGui.EndListBox();
```

## Tabs

```javascript
// Tabs
ImGui.BeginTabBar("id");  // returns true si exitoso
    ImGui.BeginTabItem("Tab 1");
        // contenido
    ImGui.EndTabItem();

    ImGui.BeginTabItem("Tab 2");
    ImGui.EndTabItem();
ImGui.EndTabBar();

// Tab Item individual
ImGui.BeginTabItem("label", open_ref);  // open_ref = returns false si cerrado
ImGui.BeginTabItem("label", null, flags);

// TabBar Flags
ImGui.TabBarFlags.Reorderable
ImGui.TabBarFlags.AutoSelectNewTabs
ImGui.TabBarFlags.TabListPopupButton
ImGui.TabBarFlags.NoCloseWithMiddleMouseButton
ImGui.TabBarFlags.FittingPolicyResizeDown
ImGui.TabBarFlags.FittingPolicyScroll

// TabItem Flags
ImGui.TabItemFlags.UnsavedDocument
ImGui.TabItemFlags.SetSelected
ImGui.TabItemFlags.NoCloseWithMiddleMouseButton
```

## Tables

```javascript
// Table básica
ImGui.BeginTable("id", column_count);
    ImGui.TableNextRow();
    ImGui.TableNextColumn(); ImGui.Text("celda 1");
    ImGui.TableNextColumn(); ImGui.Text("celda 2");
ImGui.EndTable();

// Table con headers
ImGui.BeginTable("id", 3, flags);
    ImGui.TableSetupColumn("Header 1");
    ImGui.TableSetupColumn("Header 2");
    ImGui.TableSetupColumn("Header 3");
    ImGui.TableHeadersRow();
    // rows...
ImGui.EndTable();

// Table API
ImGui.TableNextRow(row_flags, min_height);
ImGui.TableNextColumn();  // returns false si no hay más columnas
ImGui.TableSetColumnIndex(column_idx);
ImGui.TableSetupColumn(label, flags, init_width_or_weight);
ImGui.TableHeadersRow();
ImGui.TableAngledHeadersRow();
ImGui.TableSetupScrollFreeze(cols, rows);

// Table Flags
ImGui.TableFlags.Resizable
ImGui.TableFlags.Reorderable
ImGui.TableFlags.Hideable
ImGui.TableFlags.Sortable
ImGui.TableFlags.MultiSortable
ImGui.TableFlags.RowBg
ImGui.TableFlags.BordersInner
ImGui.TableFlags.BordersOuter
ImGui.TableFlags.BordersH
ImGui.TableFlags.BordersV
ImGui.TableFlags.NoHostExtendX
ImGui.TableFlags.NoHostExtendY
ImGui.TableFlags.PreciseWidths
```

## Menus

```javascript
// Menu Bar
ImGui.BeginMenuBar();
    ImGui.BeginMenu("File");
        ImGui.MenuItem("New", "Ctrl+N");
        ImGui.MenuItem("Open", "Ctrl+O", selected_ref);
        ImGui.Separator();
        ImGui.MenuItem("Exit", "Alt+F4");
    ImGui.EndMenu();

    ImGui.BeginMenu("Edit");
        ImGui.MenuItem("Copy", "Ctrl+C", null, false);  // disabled
        ImGui.MenuItem("Paste", "Ctrl+V");
    ImGui.EndMenu();
ImGui.EndMenuBar();

// Menú emergente (popup)
ImGui.BeginPopupContextItem("id");  // click derecho sobre item
ImGui.BeginPopupContextWindow("id");
ImGui.BeginPopupContextVoid("id");

// MenuItem
ImGui.MenuItem("label", shortcut, selected_ref, enabled);
// returns true si seleccionado
```

## Popups y Modals

```javascript
// Open/Close Popup
ImGui.OpenPopup("id");
ImGui.CloseCurrentPopup();

// BeginPopup (auto-close)
ImGui.BeginPopup("id");
ImGui.BeginPopupModal("id", open_ref);  // modal (bloquea input)
ImGui.EndPopup();

// Popup con condición
if (ImGui.BeginPopupContextItem("item context")) {
    ImGui.Text("Popup content");
    ImGui.EndPopup();
}

// Ejemplo de modal
ImGui.BeginPopupModal("Delete?", null, flags);
    ImGui.Text("Are you sure?");
    if (ImGui.Button("Yes")) {
        // acción
        ImGui.CloseCurrentPopup();
    }
    ImGui.SameLine();
    if (ImGui.Button("No")) {
        ImGui.CloseCurrentPopup();
    }
ImGui.EndPopup();

// PopupFlags
ImGui.PopupFlags.NoReopen
ImGui.PopupFlags.MouseButtonLeft
ImGui.PopupFlags.MouseButtonRight
ImGui.PopupFlags.MouseButtonMiddle
```

## Separators y Spacing

```javascript
ImGui.Separator();
ImGui.SeparatorText("label");  // texto con separador
ImGui.SameLine(offset_from_start, spacing);
ImGui.NewLine();
ImGui.Spacing();
ImGui.Dummy(width, height);  // espacio en blanco
ImGui.Indent(indent_w);
ImGui.Unindent(indent_w);
ImGui.BeginGroup();
ImGui.EndGroup();
```

## Images

```javascript
// Image (display)
ImGui.Image(texture_id, size);  // size: {w, h}
ImGui.Image(texture_id, size, uv0, uv1, tint_col, border_col);

// ImageButton
ImGui.ImageButton(texture_id, size);
ImGui.ImageButton("id", texture_id, size, uv0, uv1, bg_col, tint_col);

// UV coords: {x, y}
// uv0, uv1 = corners de textura (default: 0,0 a 1,1)
```

## Progress y Loading

```javascript
ImGui.ProgressBar(fraction);
ImGui.ProgressBar(fraction, size, overlay);
ImGui.ProgressBar(fraction, size_arg, "overlay text");

ImGui.Spinner(label, radius, thickness);
ImGui.Skeleton(data, size, offset);
```

## Tooltips

```javascript
// Tooltip simple
ImGui.Text("Hover me");
if (ImGui.IsItemHovered()) {
    ImGui.SetTooltip("Tooltip text!");
}

// Tooltip avanzado (más contenido)
if (ImGui.IsItemHovered()) {
    ImGui.BeginTooltip();
    ImGui.Text("Line 1");
    ImGui.Text("Line 2");
    ImGui.EndTooltip();
}
```

## Utilities

```javascript
// IDs únicos
ImGui.PushID("id");
ImGui.PopID();
ImGui.GetID("id");  // genera ID único

// Getter/Setter pattern
ImGui.SliderFloat("label", (n) => {
    if (n !== undefined) value = n;
    return value;
}, min, max);

// Verificar hover/focus/click
ImGui.IsItemHovered();     // hover actual
ImGui.IsItemActive();      // siendo arrastrado/clickeado
ImGui.IsItemFocused();     // tiene focus de keyboard
ImGui.IsItemClicked();     // fue clickeado este frame
ImGui.IsItemVisible();     // es visible
ImGui.IsItemEdited();      // fue editado este frame
ImGui.IsItemDeactivated(); // perdió focus este frame

// Item rect utilities
ImGui.GetItemRectMin();    // retorna ImVec2
ImGui.GetItemRectMax();
ImGui.GetItemRectSize();

// State utilities
ImGui.GetStateStorage();
ImGui.SetStateStorage(storage);

// Focus
ImGui.SetNextWindowFocus();
ImGui.SetNextWindowBgAlpha(alpha);
ImGui.SetKeyboardFocusHere(offset);

// Clipboard
ImGui.GetClipboardText();
ImGui.SetClipboardText(text);

// Debug
ImGui.ShowDemoWindow();  // abre ventana de demo
```

## Window Utils

```javascript
ImGui.SetNextWindowPos(x, y, cond, pivot_x, pivot_y);
ImGui.SetNextWindowSize(w, h, cond);
ImGui.SetNextWindowSizeConstraints(min_w, max_w, min_h, max_h);
ImGui.SetNextWindowContentSize(w, h);
ImGui.SetNextWindowCollapsed(collapsed, cond);
ImGui.SetNextWindowFocus();

// Cond flags
ImGui.Cond.None
ImGui.Cond.Always
ImGui.Cond.Once
ImGui.Cond.FirstUseEver
ImGui.Cond.Appearing
```

## Style

```javascript
// Colores
ImGui.GetStyle();
ImGui.GetStyle().Colors[ImGui.Col.Text];  // {r, g, b, a}

// Style colors
ImGui.Col.Text
ImGui.Col.TextDisabled
ImGui.Col.WindowBg
ImGui.Col.ChildBg
ImGui.Col.PopupBg
ImGui.Col.Border
ImGui.Col.BorderShadow
ImGui.Col.FrameBg
ImGui.Col.FrameBgHovered
ImGui.Col.FrameBgActive
ImGui.Col.TitleBg
ImGui.Col.TitleBgActive
ImGui.Col.TitleBgCollapsed
ImGui.Col.MenuBarBg
ImGui.Col.ScrollbarBg
ImGui.Col.ScrollbarGrab
ImGui.Col.ScrollbarGrabHovered
ImGui.Col.ScrollbarGrabActive
ImGui.Col.CheckMark
ImGui.Col.SliderGrab
ImGui.Col.SliderGrabActive
ImGui.Col.Button
ImGui.Col.ButtonHovered
ImGui.Col.ButtonActive
ImGui.Col.Header
ImGui.Col.HeaderHovered
ImGui.Col.HeaderActive
ImGui.Col.Separator
ImGui.Col.SeparatorHovered
ImGui.Col.SeparatorActive
ImGui.Col.Tab
ImGui.Col.TabHovered
ImGui.Col.TabActive
ImGui.Col.TabUnfocused
ImGui.Col.TabUnfocusedActive
ImGui.Col.PlotLines
ImGui.Col.PlotLinesHovered
ImGui.Col.PlotHistogram
ImGui.Col.PlotHistogramHovered
ImGui.Col.TextSelectedBg
ImGui.Col.DragDropTarget
ImGui.Col.NavHighlight
ImGui.Col.NavWindowingHighlight
ImGui.Col.NavWindowingDimBg
ImGui.Col.ModalWindowDimBg
```

## Plotting

```javascript
ImGui.PlotLines(label, values, values_offset, overlay_text, min, max, graph_size);
ImGui.PlotHistogram(label, values, values_offset, overlay_text, min, max, graph_size);
```

## Math Helpers

```javascript
// ImVec2
new ImGui.ImVec2(x, y);

// Propiedades
vec.x, vec.y
vec.add(), vec.sub(), vec.mul(), vec.div()
vec.Length(), vec.LengthSq()
vec.Normalize()
vec.Dot()
vec.Cross()
vec.Transform()
vec.TransformCoord()
```

## Constantes Útiles

```javascript
// Keys
ImGui.Key.Tab
ImGui.Key.LeftArrow
ImGui.Key.RightArrow
ImGui.Key.UpArrow
ImGui.Key.DownArrow
ImGui.Key.PageUp
ImGui.Key.PageDown
ImGui.Key.Home
ImGui.Key.End
ImGui.Key.Insert
ImGui.Key.Delete
ImGui.Key.Backspace
ImGui.Key.Space
ImGui.Key.Enter
ImGui.Key.Escape
ImGui.Key.A // Ctrl+A, etc.

// Mouse buttons
ImGui.MouseButton.Left
ImGui.MouseButton.Right
ImGui.MouseButton.Middle
```

## Ejemplo Completo

```javascript
function loop(time) {
    ImGui_Impl.NewFrame(time);
    ImGui.NewFrame();

    // Ventana principal
    ImGui.SetNextWindowPos({x: 10, y: 10}, ImGui.Cond.Once);
    ImGui.SetNextWindowSize({x: 300, y: 400}, ImGui.Cond.Once);

    ImGui.Begin("Mi App");

    // Slider
    ImGui.Text("Ajustes");
    ImGui.SliderFloat("Volumen", (n) => {
        if (n !== undefined) volume = n;
        return volume;
    }, 0, 100);

    // Checkbox
    ImGui.Checkbox("Activar", (v) => {
        if (v !== undefined) active = v;
        return active;
    });

    // Combo
    ImGui.Combo("Modo", (i) => {
        if (i !== undefined) mode = i;
        return mode;
    }, ["Normal", "Rapido", "Preciso"]);

    // Tree
    if (ImGui.TreeNode("Opciones Avanzadas")) {
        ImGui.Checkbox("Opcion 1", (v) => opt1 = v ?? opt1);
        ImGui.Checkbox("Opcion 2", (v) => opt2 = v ?? opt2);
        ImGui.TreePop();
    }

    // Button
    if (ImGui.Button("Ejecutar")) {
        console.log("Ejecutando...");
    }

    ImGui.End();

    ImGui.EndFrame();
    ImGui.Render();
    ImGui_Impl.RenderDrawData(ImGui.GetDrawData());
}
```