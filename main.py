import tkinter as tk
from tkinter import ttk
from gui import IntroductionTab, ParameterSetsTab, ResultsTab
from data import MarketData
from report import ReportGenerator

class EnhancedReportGeneratorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Enhanced Report Generator")
        self.master.geometry("1000x900")

        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.market_data = MarketData()

        self.intro_tab = IntroductionTab(self.notebook, self.market_data)
        self.param_tab = ParameterSetsTab(self.notebook)
        self.results_tab = ResultsTab(self.notebook, self.market_data)

        self.intro_tab.add_observer(self.results_tab.on_market_change)

        self.generate_button = tk.Button(master, text="Generate Report", command=self.generate_report)
        self.generate_button.pack(pady=10)

    def generate_report(self):
        report_generator = ReportGenerator(self.intro_tab, self.param_tab, self.results_tab)
        report_generator.generate()

if __name__ == "__main__":
    root = tk.Tk()
    app = EnhancedReportGeneratorGUI(root)
    root.mainloop()