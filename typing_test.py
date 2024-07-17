import time
from tkinter import *
from tkinter import ttk, scrolledtext, messagebox

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("900x600")
        self.root.config(bg="#4CAF50")  # Green background

        self.user_name = StringVar()
        self.selected_topic = StringVar()
        self.selected_time = IntVar(value=1)  # Default time selection is 1 minute
        self.start_time = None
        self.end_time = None

        self.paragraphs = {
            "Python": """Python is a high-level, interpreted programming language with dynamic semantics and simple syntax. Python's design philosophy emphasizes readability and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java. Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming styles. It features a dynamic type system and automatic memory management and has a large and comprehensive standard library.

Python is widely used in various domains such as web development (like Django and Flask), scientific computing (with libraries like NumPy and SciPy), artificial intelligence (using frameworks like TensorFlow and PyTorch), and data analysis (with tools like pandas and Matplotlib).

Learning Python can significantly enhance your career opportunities in today's technology-driven world.""",
            "Machine Learning": """Machine learning is the scientific study of algorithms and statistical models that computer systems use to perform specific tasks without using explicit instructions, relying on patterns and inference instead. It is seen as a subset of artificial intelligence. Machine learning algorithms build a mathematical model based on sample data, known as training data, in order to make predictions or decisions without being explicitly programmed to perform the task.

Machine learning is used in various applications such as recommendation systems (like Netflix's recommendation algorithm), natural language processing (NLP), image and speech recognition, autonomous vehicles, and medical diagnosis.

Mastering machine learning concepts and algorithms can open doors to exciting career opportunities in fields such as data science, robotics, and AI research.""",
            "Data Scientist": """A data scientist is a professional responsible for collecting, analyzing, and interpreting large amounts of data to identify ways to help a business improve operations and gain a competitive edge over rivals. Data scientists use advanced analytics technologies, including machine learning and predictive modeling, to extract insights from data. They work across industries to solve complex problems and guide strategic decisions.

Data scientists possess skills in programming (Python, R, SQL), statistical analysis, machine learning, data visualization (using tools like Tableau or Matplotlib), and domain expertise in fields like finance, healthcare, or marketing.

Becoming a data scientist requires a combination of technical skills, analytical mindset, and domain knowledge to effectively leverage data for business success."""
        }

        self.create_welcome_screen()

    def create_welcome_screen(self):
        self.clear_screen()

        Label(self.root, text="Welcome to Typing Speed Test", font=("Arial", 24, "bold"), bg="#4CAF50", fg="white").pack(pady=20)

        Label(self.root, text="Enter your name:", font=("Arial", 18), bg="#4CAF50", fg="white").pack(pady=10)
        Entry(self.root, textvariable=self.user_name, font=("Arial", 16)).pack(pady=10)

        Button(self.root, text="Continue", font=("Arial", 16, "bold"), bg="white", fg="#4CAF50", command=self.create_topic_screen).pack(pady=20)

    def create_topic_screen(self):
        if not self.user_name.get():
            messagebox.showerror("Error", "Please enter your name")
            return

        self.clear_screen()

        Label(self.root, text="Select a Topic", font=("Arial", 24, "bold"), bg="#4CAF50", fg="white").pack(pady=20)

        topic_combo = ttk.Combobox(self.root, textvariable=self.selected_topic, values=list(self.paragraphs.keys()), font=("Arial", 16))
        topic_combo.pack(pady=10)
        topic_combo.config(background="white", width=30)  # White background for combo box

        Label(self.root, text="Select Test Duration (minutes):", font=("Arial", 18), bg="#4CAF50", fg="white").pack(pady=10)
        time_combo = ttk.Combobox(self.root, textvariable=self.selected_time, values=list(range(1, 11)), font=("Arial", 16))
        time_combo.pack(pady=10)
        time_combo.config(background="white", width=30)  # White background for combo box

        Button(self.root, text="Start Test", font=("Arial", 16, "bold"), bg="white", fg="#4CAF50", command=self.create_test_screen).pack(pady=20)

    def create_test_screen(self):
        if not self.selected_topic.get():
            messagebox.showerror("Error", "Please select a topic")
            return

        self.clear_screen()

        # Create frames for layout
        top_frame = Frame(self.root, bg="#4CAF50")
        top_frame.pack(side=TOP, fill=X)

        left_frame = Frame(self.root, bg="white", padx=20, pady=20)
        left_frame.pack(side=TOP, fill=BOTH, expand=True)

        right_frame = Frame(self.root, bg="white", padx=20, pady=20)
        right_frame.pack(side=TOP, fill=BOTH, expand=True)

        # Timer display at the top
        self.timer_label = Label(top_frame, text=f"Time Remaining: {self.selected_time.get()}:00", font=("Arial", 16, "bold"), bg="#4CAF50", fg="white")
        self.timer_label.pack(pady=10)

        # Create a scrolled text widget for paragraph display
        self.paragraph_text = scrolledtext.ScrolledText(left_frame, font=("Arial", 16), wrap=WORD, bd=2, relief=GROOVE, width=100, height=10)
        self.paragraph_text.pack(pady=20, padx=20, fill=BOTH, expand=True)
        self.paragraph_text.insert(END, self.paragraphs[self.selected_topic.get()])
        self.paragraph_text.config(state=DISABLED)  # Disable editing

        # Typing area 
        Label(right_frame, text="Start typing here:", font=("Arial", 18, "bold"), bg="white", fg="#4CAF50").pack(anchor=W)

        self.typing_area = Text(right_frame, font=("Arial", 16), wrap=WORD, bd=2, relief=GROOVE, width=100, height=15)
        self.typing_area.pack(pady=20, padx=20, fill=BOTH, expand=True)
        self.typing_area.bind("<KeyPress>", self.start_timer)

        # Submit button
        Button(self.root, text="End Test and Submit", font=("Arial", 16, "bold"), bg="#4CAF50", fg="white", command=self.calculate_speed).pack(pady=20)

        # Start the timer countdown
        self.start_time = time.time()
        self.remaining_time_loop()

    def remaining_time_loop(self):
        if self.start_time:
            elapsed_time = time.time() - self.start_time
            remaining_seconds = max(0, self.selected_time.get() * 60 - int(elapsed_time))
            minutes = remaining_seconds // 60
            seconds = remaining_seconds % 60
            self.timer_label.config(text=f"Time Remaining: {minutes:02}:{seconds:02}")

            if remaining_seconds > 0:
                self.root.after(1000, self.remaining_time_loop)
            else:
                self.calculate_speed()

    def start_timer(self, event):
        if not self.start_time:
            self.start_time = time.time()

    def calculate_speed(self, event=None):
        if self.end_time is None:
            self.end_time = time.time()

        typed_text = self.typing_area.get(1.0, END).strip()
        original_text = self.paragraphs[self.selected_topic.get()]

        if not typed_text:
            messagebox.showerror("Error", "Please type the paragraph")
            return

        typed_lines = typed_text.splitlines()
        original_lines = original_text.splitlines()

        total_words = 0
        correct_words = 0

        for typed_line, original_line in zip(typed_lines, original_lines):
            typed_words = typed_line.split()
            original_words = original_line.split()
            
            for typed_word, original_word in zip(typed_words, original_words):
                total_words += 1
                if typed_word == original_word:
                    correct_words += 1

        accuracy = (correct_words / total_words) * 100 if total_words > 0 else 0

        elapsed_time = self.end_time - self.start_time
        words_typed = len(typed_text.split())
        typing_speed = words_typed / (elapsed_time / 60)

        self.show_result(typing_speed, accuracy)

    def show_result(self, speed, accuracy):
        self.clear_screen()

        Label(self.root, text=f"Congratulations, {self.user_name.get()}!", font=("Arial", 24, "bold"), bg="#4CAF50", fg="white").pack(pady=20)
        Label(self.root, text=f"Your typing speed is {speed:.2f} words per minute", font=("Arial", 18), bg="white", fg="#4CAF50").pack(pady=10)
        Label(self.root, text=f"Accuracy: {accuracy:.2f}%", font=("Arial", 18), bg="white", fg="#4CAF50").pack(pady=10)

        Button(self.root, text="Try Again", font=("Arial", 16, "bold"), bg="#4CAF50", fg="white", command=self.create_welcome_screen).pack(pady=20)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
