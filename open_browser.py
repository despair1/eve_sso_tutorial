import webbrowser
import config_init_full_path

configuration = config_init_full_path.config_init

url = configuration.get("login_user_url")
url += r'/?response_type=code&'
url += r'redirect_uri='+configuration.get("CallbackURL")
url += r'&client_id='+configuration.get("ClientID")
url += r'&scope='+configuration.get("scope")
url += r'&state=lamerzNeverDie'


webbrowser.open(url)