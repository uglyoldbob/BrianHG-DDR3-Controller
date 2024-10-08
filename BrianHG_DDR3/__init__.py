import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = __dir__
src = "https://github.com/BrianHGinc/BrianHG-DDR3-Controller.git"

# Module version
version_str = "1.65"
version_tuple = (1, 65, 0, 0)
try:
    from packaging.version import Version as V
    pversion = V("1.65")
except ImportError:
    pass

# Data version info
data_version_str = "1.65"
data_version_tuple = (1, 0, 1)
try:
    from packaging.version import Version as V
    pdata_version = V("1.65")
except ImportError:
    pass
data_git_hash = "5f0c7a7faf6b65c907a93be6e3723e297d37ee71"
data_git_describe = "v1.65"
data_git_msg = """\

"""

# Tool version info
tool_version_str = "1.65"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("1.65")
except ImportError:
    pass

def data_file(f):
    """Get absolute path for file inside brianhg_ddr3."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in brianhg_ddr3".format(f))
    return fn

class Ddr3:
    def __init__(self, platform):
        platform.add_source(os.path.join(data_location, "BrianHG_DDR3_PHY_SEQ_v16.sv"))
        platform.add_source(os.path.join(data_location, "BrianHG_DDR3_GEN_tCK.sv"))
        platform.add_source(os.path.join(data_location, "BrianHG_DDR3_CMD_SEQUENCER_v16.sv"))
        platform.add_source(os.path.join(data_location, "BrianHG_DDR3_PLL.sv"))
        platform.add_source(os.path.join(data_location, "BrianHG_DDR3_FIFOs.sv"))
        platform.add_source(os.path.join(data_location, "BrianHG_DDR3_IO_PORT_ALTERA.sv"))
        platform.add_source(os.path.join(data_location, "BrianHG_DDR3_CONTROLLER_v16_top.sv"))
        platform.add_source(os.path.join(data_location, "BrianHG_DDR3_COMMANDER_v16.sv"))
        platform.add_source(os.path.join(data_location, "altera_gpio_lite.sv"))

