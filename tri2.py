import tkinter as tk
import random

class DeadlockDetectionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Deadlock Detection")
        self.processes = 3
        self.resources = 4
        self.allocate_matrix = [[0, 1, 0, 1],
                                [1, 0, 1, 0],
                                [0, 1, 0, 1]]
        self.request_matrix = [[1, 0, 1, 0],
                               [0, 1, 0, 1],
                               [1, 0, 1, 0]]
        self.resources_available = [2, 2, 2, 2]

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Allocation Matrix").pack()

        self.allocate_frame = tk.Frame(self.root)
        self.allocate_frame.pack()

        for i in range(self.processes):
            row = []
            for j in range(self.resources):
                entry = tk.Entry(self.allocate_frame, width=5)
                entry.insert(tk.END, self.allocate_matrix[i][j])
                entry.configure(state='readonly')
                entry.pack(side=tk.LEFT)
                row.append(entry)
            self.allocate_matrix.append(row)

        tk.Label(self.root, text="\nRequest Matrix").pack()

        self.request_frame = tk.Frame(self.root)
        self.request_frame.pack()

        for i in range(self.processes):
            row = []
            for j in range(self.resources):
                entry = tk.Entry(self.request_frame, width=5)
                entry.insert(tk.END, self.request_matrix[i][j])
                entry.configure(state='readonly')
                entry.pack(side=tk.LEFT)
                row.append(entry)
            self.request_matrix.append(row)

        tk.Label(self.root, text="\nResource Availability").pack()

        self.resources_frame = tk.Frame(self.root)
        self.resources_frame.pack()

        for i in range(self.resources):
            entry = tk.Entry(self.resources_frame, width=5)
            entry.insert(tk.END, self.resources_available[i])
            entry.configure(state='readonly')
            entry.pack(side=tk.LEFT)

        tk.Button(self.root, text="Randomize Matrix", command=self.randomize_matrices).pack()
        tk.Button(self.root, text="Run Detection", command=self.run_detection).pack()

        tk.Label(self.root, text="\nExplanation/Output:").pack()
        self.explanation_text = tk.Text(self.root, height=10, width=50)
        self.explanation_text.pack()

    def randomize_matrices(self):
        self.allocate_matrix = [[random.randint(0, 1) for _ in range(self.resources)] for _ in range(self.processes)]
        self.request_matrix = [[random.randint(0, 1) for _ in range(self.resources)] for _ in range(self.processes)]
        self.resources_available = [random.randint(0, 5) for _ in range(self.resources)]

        self.update_matrices()
        self.clear_output()

    def update_matrices(self):
        for row_frame in [self.allocate_frame, self.request_frame]:
            for widget in row_frame.winfo_children():
                widget.destroy()

        for i in range(self.processes):
            for j in range(self.resources):
                entry = tk.Entry(self.allocate_frame, width=5)
                entry.insert(tk.END, self.allocate_matrix[i][j])
                entry.configure(state='readonly')
                entry.pack(side=tk.LEFT)

        for i in range(self.processes):
            for j in range(self.resources):
                entry = tk.Entry(self.request_frame, width=5)
                entry.insert(tk.END, self.request_matrix[i][j])
                entry.configure(state='readonly')
                entry.pack(side=tk.LEFT)

        for widget in self.resources_frame.winfo_children():
            widget.destroy()

        for i in range(self.resources):
            entry = tk.Entry(self.resources_frame, width=5)
            entry.insert(tk.END, self.resources_available[i])
            entry.configure(state='readonly')
            entry.pack(side=tk.LEFT)

    def clear_output(self):
        self.explanation_text.delete(1.0, tk.END)

    def run_detection(self):
        deadlock_detected = self.detect_deadlock()
        if deadlock_detected:
            explanation = "DEADLOCK DETECTED!"
            self.highlight_deadlock()
        else:
            explanation = "No Deadlock Detected."
        self.display_output(explanation)

    def detect_deadlock(self):
        explanation = ""

        step_1 = "Step 1: Checking resource allocation..."
        explanation += step_1 + "\n"
        # Your deadlock detection algorithm logic here...

        step_2 = "Step 2: Analyzing resource requests..."
        explanation += step_2 + "\n"
        # Your deadlock detection algorithm logic here...

        step_3 = "Step 3: Verifying resource availability..."
        explanation += step_3 + "\n"
        # Your deadlock detection algorithm logic here...

        # Replace the return statement with the actual condition for deadlock detection
        deadlock_detected = random.choice([True, False])

        if deadlock_detected:
            explanation += "DEADLOCK DETECTED!"
            self.highlight_deadlock()
        else:
            explanation += "No Deadlock Detected."

        self.display_output(explanation)
        return deadlock_detected

    def highlight_deadlock(self):
        for row in self.allocate_matrix:
            for entry in row:
                entry.configure(bg='red')

        for row in self.request_matrix:
            for entry in row:
                entry.configure(bg='red')

        for entry in self.resources_frame.winfo_children():
            entry.configure(bg='red')

    def display_output(self, explanation):
        self.explanation_text.delete(1.0, tk.END)
        self.explanation_text.insert(tk.END, explanation)

def main():
    root = tk.Tk()
    app = DeadlockDetectionGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
