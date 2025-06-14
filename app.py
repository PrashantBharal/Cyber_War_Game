import tkinter as tk
from tkinter import ttk
from scenarios import (
    scenario_phishing_cyberwar,
    scenario_ddos_cyberwar,
    scenario_ransomware_cyberwar,
    scenario_bec_cyberwar,
    scenario_password_spray_cyberwar,
    scenario_insider_threat_cyberwar,
)

# Constants
WRAP_LENGTH = 400
BUBBLE_MAX_WIDTH = 500
BLUE_BUBBLE_COLOR = '#D0E8FF'
GREEN_BUBBLE_COLOR = '#DCF8C6'
OTHER_BUBBLE_COLOR = '#FFFFFF'
BUBBLE_FONT = ("Arial", 12)
BUBBLE_PADDING_X = 10
BUBBLE_PADDING_Y = 5
BUBBLE_CORNER_RADIUS = 15
OFF_WHITE = '#F5F5F5'

class CyberWarGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cyber War Game")
        self.root.configure(bg="black")
        try:
            self.root.state('zoomed')
        except:
            self.root.attributes('-fullscreen', True)

        self.user_name = tk.StringVar()
        self.phase_index = 0
        self.question_index = 0
        self.answered = False
        self.history = []
        self.current_scenario = None
        self.correct_count = 0
        self.wrong_count = 0

        self.scenario_map = {
            "Phishing": scenario_phishing_cyberwar,
            "DDoS": scenario_ddos_cyberwar,
            "Ransomware": scenario_ransomware_cyberwar,
            "BEC": scenario_bec_cyberwar,
            "Password": scenario_password_spray_cyberwar,
            "Insider": scenario_insider_threat_cyberwar,
        }
        self.show_name_screen()

    def draw_white_box(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        canvas = tk.Canvas(self.root, bg="black", highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        frame = tk.Frame(canvas, bg=OFF_WHITE)
        window_id = canvas.create_window((0,0), window=frame, anchor='center')

        def on_configure(e):
            w, h = e.width, e.height
            canvas.delete('bg')
            pts = [
                30+BUBBLE_CORNER_RADIUS, 30,
                w-30-BUBBLE_CORNER_RADIUS, 30,
                w-30, 30,
                w-30, 30+BUBBLE_CORNER_RADIUS,
                w-30, h-30-BUBBLE_CORNER_RADIUS,
                w-30, h-30,
                w-30-BUBBLE_CORNER_RADIUS, h-30,
                30+BUBBLE_CORNER_RADIUS, h-30,
                30, h-30,
                30, h-30-BUBBLE_CORNER_RADIUS,
                30, 30+BUBBLE_CORNER_RADIUS,
                30, 30
            ]
            canvas.create_polygon(pts, fill=OFF_WHITE, outline=OFF_WHITE, smooth=True, tags='bg')
            canvas.coords(window_id, w/2, h/2)
        canvas.bind('<Configure>', on_configure)
        return frame

    def _rounded_rect_points(self, x1, y1, x2, y2, r):
        return [
            x1+r, y1, x2-r, y1, x2, y1, x2, y1+r,
            x2, y2-r, x2, y2, x2-r, y2, x1+r, y2,
            x1, y2, x1, y2-r, x1, y1+r, x1, y1
        ]

    def show_name_screen(self):
        f = self.draw_white_box()
        tk.Label(f, text="Cyber War Game", font=("Arial",24,'bold'), bg=OFF_WHITE).pack(pady=(80,20))
        tk.Label(f, text="Enter your name:", font=("Arial",12), bg=OFF_WHITE).pack()
        e = tk.Entry(f, textvariable=self.user_name, font=("Arial",12), width=40,
                     justify='center', bg='#f5f5f5', relief='flat')
        e.pack(pady=(5,40))
        e.focus_set()
        e.bind('<Return>', lambda ev: self.on_name_entered())
        tk.Button(f, text="Continue", font=("Arial",12,'bold'), bg='#00B386', fg='white',
                  width=24, relief='flat', command=self.on_name_entered).pack()

    def on_name_entered(self):
        if self.user_name.get().strip():
            self.show_dashboard()

    def show_dashboard(self):
        f = self.draw_white_box()
        tk.Label(f, text=f"Welcome {self.user_name.get()}!", font=("Arial",20,'bold'), bg=OFF_WHITE).pack(pady=(20,10))
        tk.Label(f, text="Select a scenario:", font=("Arial",14), bg=OFF_WHITE).pack(pady=(0,10))
        bf = tk.Frame(f, bg=OFF_WHITE)
        bf.pack()
        for i, name in enumerate(self.scenario_map):
            btn = tk.Button(bf, text=name, font=("Arial",12,'bold'), bg='#007AFF', fg='white',
                            width=16, pady=6, relief='flat', command=lambda n=name: self.start_scenario(n))
            btn.grid(row=i//3, column=i%3, padx=8, pady=8)

    def start_scenario(self, name):
        self.current_scenario = self.scenario_map[name]
        self.phase_index = 0
        self.question_index = 0
        self.answered = False
        self.history.clear()
        self.correct_count = 0
        self.wrong_count = 0
        self.show_phase()

    def show_phase(self):
        f = self.draw_white_box()
        ph = self.current_scenario.phases[self.phase_index]
        tk.Label(f, text=ph['phase_title'], font=("Arial",18,'bold'), bg=OFF_WHITE).pack(pady=(20,5))
        tk.Label(f, text=ph['brief'], font=("Arial",12), wraplength=700, justify='center', bg=OFF_WHITE).pack(pady=(0,20))
        tk.Button(f, text="Begin Phase", font=("Arial",12,'bold'), bg='#00B386', fg='white', width=24,
                  relief='flat', command=self.show_dialogue).pack()

    def show_dialogue(self):
        f = self.draw_white_box()
        ph = self.current_scenario.phases[self.phase_index]
        tk.Label(f, text=ph['phase_title'], font=("Arial",18,'bold'), bg=OFF_WHITE).pack(pady=(5,2))
        tk.Label(f, text=ph['brief'], font=("Arial",12), wraplength=700, justify='center', bg=OFF_WHITE).pack(pady=(0,8))

        ctr = tk.Frame(f, bg=OFF_WHITE)
        ctr.pack(fill='both', expand=True, padx=20, pady=(0,10))
        cv = tk.Canvas(ctr, bg=OFF_WHITE, highlightthickness=0)
        sb = ttk.Scrollbar(ctr, orient='vertical', command=cv.yview)
        sb.pack(side='right', fill='y')
        cv.configure(yscrollcommand=sb.set)
        cv.pack(side='left', fill='both', expand=True)
        cf = tk.Frame(cv, bg=OFF_WHITE)
        wid = cv.create_window((0,0), window=cf, anchor='n')
        cv.bind('<Configure>', lambda e: cv.coords(wid, e.width/2, 0))
        cf.bind('<Configure>', lambda e: cv.configure(scrollregion=cv.bbox('all')))
        cv.bind_all('<MouseWheel>', lambda e: cv.yview_scroll(int(-1*(e.delta/120)), 'units'))
        self.root.bind('<Up>', lambda e: cv.yview_scroll(-1, 'units'))
        self.root.bind('<Down>', lambda e: cv.yview_scroll(1, 'units'))

        if not self.answered:
            for s, t in ph['questions'][self.question_index]['dialogue']:
                self.history.append(('d', s, t))

        for idx, (typ, sp, txt) in enumerate(self.history):
            if sp == self.user_name.get():
                ah, ac, tc = 'e', OTHER_BUBBLE_COLOR, 'black'
            elif sp == 'System':
                ah, ac = 'n', OTHER_BUBBLE_COLOR
                tc = 'green' if 'Correct:' not in txt else 'red'
            else:
                ah = 'w' if idx % 2 == 0 else 'e'
                ac = BLUE_BUBBLE_COLOR if ah == 'w' else GREEN_BUBBLE_COLOR
                tc = 'black'

            en = tk.Frame(cf, bg=OFF_WHITE)
            en.pack(pady=5, anchor='center', fill='x')
            if sp not in (self.user_name.get(), 'System'):
                tk.Label(en, text=sp, font=("Arial",10,'bold'), bg=OFF_WHITE).pack(anchor=ah, padx=20)

            b = tk.Canvas(en, bg=OFF_WHITE, highlightthickness=0)
            tmp = tk.Label(b, text=txt, font=BUBBLE_FONT, wraplength=WRAP_LENGTH, bg=OFF_WHITE)
            tmp.update_idletasks()
            w_, h_ = min(tmp.winfo_reqwidth(), BUBBLE_MAX_WIDTH), tmp.winfo_reqheight()
            tmp.destroy()
            b.config(width=w_+2*BUBBLE_PADDING_X, height=h_+2*BUBBLE_PADDING_Y)
            b.create_polygon(*self._rounded_rect_points(0,0,w_+2*BUBBLE_PADDING_X,h_+2*BUBBLE_PADDING_Y,BUBBLE_CORNER_RADIUS), fill=ac, outline=ac, smooth=True)
            b.create_text(BUBBLE_PADDING_X, BUBBLE_PADDING_Y, text=txt, font=BUBBLE_FONT, anchor='nw', fill=tc, width=w_)
            b.pack(anchor=ah, padx=20)

        cv.update_idletasks()
        cv.yview_moveto(1.0)
        btn_text = "Answer" if not self.answered else "Next"
        btn_color = '#007AFF' if not self.answered else '#00B386'
        tk.Button(f, text=btn_text, font=("Arial",12,'bold'), bg=btn_color, fg='white', width=24, relief='flat',
                  command=(self.show_mcq if not self.answered else self.advance_question)).pack(pady=(0,20))

    def show_mcq(self):
        f = self.draw_white_box()
        q = self.current_scenario.phases[self.phase_index]['questions'][self.question_index]
        tk.Label(f, text=q.get('question',''), font=("Arial",14,'bold'), wraplength=WRAP_LENGTH, justify='center', bg=OFF_WHITE).pack(pady=(20,20))
        for i, opt in enumerate(q['options']):
            tk.Button(f, text=opt, font=("Arial",10), wraplength=WRAP_LENGTH, width=50,
                      bg='#00B386', fg='white', relief='flat', command=lambda i=i: self.check_answer(i)).pack(pady=5, padx=20)

    def check_answer(self, choice):
        q = self.current_scenario.phases[self.phase_index]['questions'][self.question_index]
        correct = (choice == q['correct_index'])
        self.history.append(('d', self.user_name.get(), f"Your answer: {q['options'][choice]}"))
        feedback = q['outcome_correct'] if correct else f"{q['outcome_wrong']}. Correct: {q['options'][q['correct_index']]}"
        self.history.append(('d', 'System', feedback))
        if correct:
            self.correct_count += 1
        else:
            self.wrong_count += 1
        self.answered = True
        self.show_dialogue()

    def advance_question(self):
        self.question_index += 1
        self.answered = False
        if self.question_index >= len(self.current_scenario.phases[self.phase_index]['questions']):
            self.phase_index += 1
            self.question_index = 0
            if self.phase_index >= len(self.current_scenario.phases):
                return self.end_game()
            return self.show_phase()
        self.show_dialogue()

    def end_game(self):
        f = self.draw_white_box()
        total = self.correct_count + self.wrong_count
        pct = (self.correct_count / total * 100) if total else 0
        tk.Label(f, text="🏁 Simulation Complete!", font=("Arial",20,'bold'), bg=OFF_WHITE).pack(pady=(40,10))
        tk.Label(f, text=f"Correct Answers: {self.correct_count}", font=("Arial",14), fg='green', bg=OFF_WHITE).pack()
        tk.Label(f, text=f"Wrong Answers: {self.wrong_count}", font=("Arial",14), fg='red', bg=OFF_WHITE).pack()
        tk.Label(f, text=f"Score: {pct:.1f}%", font=("Arial",16,'bold'), bg=OFF_WHITE).pack(pady=(10,20))
        tk.Label(f, text=f"Thanks for playing, {self.user_name.get()}!", font=("Arial",14), bg=OFF_WHITE).pack(pady=(0,40))


def run_gui_game():
    root = tk.Tk()
    CyberWarGameGUI(root)
    root.mainloop()
