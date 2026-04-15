import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

gi.require_version('Adap', '1')
from gi.repository import Adap as Adw

# To use libAdwaita, we would import this instead:
# gi.require_version('Adw', '1')
# from gi.repository import Adw

class AppList(Gtk.Box):
    def __init__(self, **kwargs):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        self.set_hexpand(True)
        self.set_vexpand(True)

        # Lista desplazable de aplicaciones
        # Este muestra el listado de aplicaciones disponibles para 
        # descarga con su informacion. Este es añadido dentro de un 
        # ScrolledWindow para que dicho control muestre barras de 
        # desplazamiento conforme crece
        self.app_listbox = Gtk.ListBox()
        self.app_listbox.set_selection_mode(Gtk.SelectionMode.SINGLE)
        self.app_scrollview = Gtk.ScrolledWindow()
        self.app_scrollview.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        self.app_scrollview.set_hexpand(True)
        self.app_scrollview.set_vexpand(True)
        self.app_scrollview.set_child(self.app_listbox)

        # Barra inferior de controles (+,-, descarga)
        self.control_bar = Gtk.Box(halign=Gtk.Align.CENTER, spacing=6)
        self.control_bar.set_margin_top(10)
        self.control_bar.set_margin_bottom(10)

        # Boton + para añadir
        add_button = Gtk.Button()
        add_button.set_icon_name("xsi-list-add-symbolic")
        #add_button.connect("clicked", self.sm_toggle_log)

        # Boton - para eliminar
        remove_button = Gtk.Button()
        remove_button.set_icon_name("xsi-list-remove-symbolic")
        #remove_button.connect("clicked", self.sm_toggle_log)

        # Boton para descarga
        download_button = Gtk.Button()
        download_button.set_icon_name("xsi-media-playback-start-symbolic")
        #download_button.connect("clicked", self.sm_toggle_log)

        # Añadir los botones a la barra de controles
        self.control_bar.append(add_button)
        self.control_bar.append(remove_button)
        self.control_bar.append(download_button)
        
        # Add page with all sections to inherited Gtk.Box
        self.append(self.app_scrollview)
        self.append(self.control_bar)