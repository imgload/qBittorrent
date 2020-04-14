import os, psutil, IPython, uuid, time
import ipywidgets as widgets

from IPython.display import HTML, clear_output
from urllib.request import urlopen
from google.colab import output

class MakeButton(object):
  def __init__(self, title, callback):
    self._title = title
    self._callback = callback
  def _repr_html_(self):
    callback_id = 'button-' + str(uuid.uuid4())
    output.register_callback(callback_id, self._callback)
    template = """<button class="p-Widget jupyter-widgets jupyter-button widget-button mod-info" id="{callback_id}">{title}</button>
        <script>
          document.querySelector("#{callback_id}").onclick = (e) => {{
            google.colab.kernel.invokeFunction('{callback_id}', [], {{}})
            e.preventDefault();
          }};
        </script>"""
    html = template.format(title=self._title, callback_id=callback_id)
    return html
  
def MakeLabel(description, button_style):
  return widgets.Button(description=description, disabled=True, button_style=button_style)

def RandomGenerator():
  return time.strftime("%S") + str(time.time()).split(".")[-1]

def CheckProcess(process, command):
  for pid in psutil.pids():
    try:
      p = psutil.Process(pid)
      if process in p.name():
        for arg in p.cmdline():
          if command in str(arg):  
            return True
          else:
            pass
      else:
        pass
    except:
      continue

def Plugin_Installer(url):
  with urlopen(url) as story:
    story_words = []
    for line in story:
      line_words = line.decode('utf-8').split()
      for word in line_words:
        story_words.append(word)
    for word in story_words:
      get_ipython().system_raw("wget -q -P /root/.local/share/data/qBittorrent/nova3/engines/ " + word + " &")
  
def AutoSSH(name,port):
  get_ipython().system_raw("autossh -M 0 -fNT -o 'StrictHostKeyChecking=no' -o 'ServerAliveInterval 300' -o 'ServerAliveCountMax 30' -R " + name + ":80:localhost:" + port + " serveo.net &")

def Start_AutoSSH_QB():
  if CheckProcess("qbittorrent-nox", "") != True:
    get_ipython().system_raw("qbittorrent-nox -d --webui-port=$Port_QB")
  if CheckProcess("autossh", Random_URL_QB) != True:
      AutoSSH(Random_URL_QB, Port_QB)

def Start_Localhost_QB():
  try:
    clear_output(wait=True)
    !autossh -l $Random_URL_QB -M 0 -o 'StrictHostKeyChecking=no' -o 'ServerAliveInterval 300' -o 'ServerAliveCountMax 30' -R 80:localhost:$Port_QB ssh.localhost.run
  except:
    Control_Panel_QB()
  Control_Panel_QB()

def Control_Panel_QB():
  clear_output(wait=True)
  display(MakeLabel("✔ Successfully", "success"), MakeButton("Web Link", Start_Localhost_QB), HTML("<h2 style=\"font-family:Trebuchet MS;color:#4f8bd6;\">qBittorrent Edit by imgload.ir</h2><h4 style=\"font-family:Trebuchet MS;color:#4f8bd6;\">"))

try:
  try:
    Random_URL_QB
  except NameError:
    Random_URL_QB = "qb" + RandomGenerator()
    Port_QB = "6006"
    display(MakeLabel("Installing in Progress", "warning"))
    get_ipython().system_raw("rm -rf /content/sample_data/")
    if Version != "4.0.3":
      get_ipython().system_raw("mkdir -p -m 666 /root/.local/share/data/qBittorrent/nova3/engines/")
      Plugin_Installer("https://raw.githubusercontent.com/imgload/qBittorrent/master/res/plugins.txt")
  if os.path.isfile("/usr/bin/autossh") == False:
    get_ipython().system_raw("apt update -qq -y && apt install autossh -qq -y")
  if os.path.isfile("/usr/bin/qbittorrent-nox") == False:
    if Version != "Newest":
      if Version == "4.0.3":
        get_ipython().system_raw("apt install qbittorrent-nox=4.0.3-1 -qq -y")
      else:
        get_ipython().system_raw("apt install libtorrent-rasterbar9 -qq -y && wget -q https://raw.githubusercontent.com/imgload/qBittorrent/master/res/archive/qbittorrent-nox_$Version\.deb -O /root/.qbittorrent-nox.deb && dpkg -i /root/.qbittorrent-nox.deb && rm -rf /root/.qbittorrent-nox.deb")
    else:
      get_ipython().system_raw("yes "" | add-apt-repository ppa:qbittorrent-team/qbittorrent-stable && apt install qbittorrent-nox -qq -y")
    get_ipython().system_raw("mkdir -p -m 666 /{content/qBittorrent,root/{.qBittorrent_temp,.config/qBittorrent}} && wget -q https://raw.githubusercontent.com/imgload/qBittorrent/master/res/qBittorrent.conf -O /root/.config/qBittorrent/qBittorrent.conf")
  Start_AutoSSH_QB()
  Control_Panel_QB()
except:
  clear_output(wait=True)
  display(MakeLabel("✘ Unsuccessfully", "danger"))