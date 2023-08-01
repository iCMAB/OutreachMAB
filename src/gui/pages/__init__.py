from .bandit_explain_page import BanditExplainPage
from .intro_page import IntroPage
from .results_page import ResultsPage
from .settings_page import SettingsPage
from .simulation_page import SimulationPage
from .start_page import StartPage

PAGES = {
    "start": StartPage,
    "simulation": SimulationPage,
    "settings": SettingsPage,
    "results": ResultsPage,
    "bandits_explained": BanditExplainPage,
    "intro": IntroPage
}
