from cx_Freeze import setup, Executable


build_exe_options = {
    "packages": ["tkinter", "threading", "time", "os", "random", "matplotlib", "numpy"],
    "include_files": ["dinheirotest.gif", "iconbaco.ico"]
}

setup(
    name="BANCOGV",
    version="0.1",
    description="Seu script Python como um executável!",
    options={"build_exe": build_exe_options},
    executables=[Executable("BancoGV11.py", icon="iconbaco.ico")]  
)

