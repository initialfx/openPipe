import nuke
import openpipe

# Create OpenPipe Menu
menubar = nuke.menu("Nuke")
m = menubar.addMenu("OpenPipe")

# Add Sample Commands
m.addCommand("Version", "nuke.message(openpipe.__version__)")
m.addSeparator()
m.addCommand("Test Module", "from openpipe.nuke import sample; sample.test_nuke()")
m.addCommand("Create Blur", "from openpipe.nuke import sample; sample.create_blur_node()")

print("✅ [OpenPipe] Nuke Menu created.")
