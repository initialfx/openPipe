import os
import nuke

# Add gizmos and python tool folders to Nuke plugin path
root = os.path.dirname(__file__)

nuke.pluginAddPath(os.path.join(root, "gizmos"))
nuke.pluginAddPath(os.path.join(root, "python"))
nuke.pluginAddPath(os.path.join(root, "scripts"))

print("✅ [OpenPipe] Nuke Plugin Path initialized.")
