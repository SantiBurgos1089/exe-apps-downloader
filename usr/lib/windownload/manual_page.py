import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

gi.require_version('Adap', '1')
from gi.repository import Adap as Adw

# To use libAdwaita, we would import this instead:
# gi.require_version('Adw', '1')
# from gi.repository import Adw

class ManualDownload(Gtk.Box):
    def __init__(self, **kwargs):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        self.set_hexpand(True)
        self.set_vexpand(True)

        self.settings_page = Adw.PreferencesPage()
        self.settings_page.set_title("Descarga")

        # Manual download section
        self.manual_group = Adw.PreferencesGroup()
        self.manual_group.set_title("Descarga manual")

        # Package ID EntryRow
        self.pkgid_entry = Adw.EntryRow()
        self.pkgid_entry.set_title("ID de paquete. Ej: 7zip.7zip")
        
        # Add row to section
        self.manual_group.add(self.pkgid_entry)
        
        # Package name EntryRow
        self.pkgname_entry = Adw.EntryRow()
        self.pkgname_entry.set_title("Nombre del programa. Ej: 7zip")

        # Add row to section
        self.manual_group.add(self.pkgname_entry)

        # Package URL EntryRow
        self.pkgurl_row = Adw.EntryRow()
        self.pkgurl_row.set_title("URL del instalador. Ej: https://...")

        # Add row to section
        self.manual_group.add(self.pkgurl_row)

        # Package name EntryRow
        self.pkgoptname_entry = Adw.EntryRow()
        self.pkgoptname_entry.set_title("Nombre a guardar (opcional. Ej: 7z-x64)")

        # Add row to section
        self.manual_group.add(self.pkgoptname_entry)

        # Row para proceso de descarga
        self.download_row = Adw.ActionRow()
        self.download_row.set_title("Iniciar descarga")
        self.download_button = Gtk.Button()
        self.download_button.set_icon_name("xsi-media-playback-start-symbolic")
        #self.download_button.connect("clicked", self.sm_toggle_log)
        self.download_row.add_suffix(self.download_button)

        # Add row to section
        self.manual_group.add(self.download_row)

        # Add section with all controls to page
        self.settings_page.add(self.manual_group)
        
        # Add page with all sections to inherited Gtk.Box
        self.append(self.settings_page)