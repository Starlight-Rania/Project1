from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image



# Define the candidates and their respective pictures
candidates = [
    {
        'name': 'candidate name',
        'picture': 'uplod photo url or where it is stored',
        'votes': 0
        
    },
    {
        'name': 'candidate name',
        'picture': 'uplod photo url or where it is stored',
        'votes': 0
    },
    
    
]




def vote(candidate_index):
    candidates[candidate_index]['votes'] += 1
    messagebox.showinfo("Success", "Your vote has been recorded!")

def show_results():
    operator_password = "password"  # Change this to your desired operator password

    def authenticate():
        password = password_entry.get()
        if password == operator_password:
            results_window = Toplevel(root)
            results_window.title("Results")
            results_text = "Results:\n"
            for candidate in candidates:
                results_text += f"{candidate['name']}: {candidate['votes']} votes\n"
            results_label = Label(results_window, text=results_text)
            results_label.pack()
        else:
            messagebox.showerror("Error", "Incorrect operator password!")

    operator_password_window = Toplevel(root)
    operator_password_window.title("Operator Authentication")

    password_label = Label(operator_password_window, text="Operator Password:")
    password_label.pack()

    password_entry = Entry(operator_password_window, show="*")
    password_entry.pack()

    authenticate_button = Button(operator_password_window, text="Authenticate", command=authenticate)
    authenticate_button.pack()

# Create the main window
root = Tk()
root.title("ELECTIONS")
text_label = Label(root, text="Elect your leader", font=('Arial', 20))
text_label.pack()
#set window color
root.configure(bg='green')

# Create the candidate buttons and labels
for i, candidate in enumerate(candidates):
    # Load the candidate picture
    image = Image.open(candidate['picture'])
    image = image.resize((200, 200))
    photo = ImageTk.PhotoImage(image)

    # Create the button and label
    button = Button(root, image=photo, command=lambda i=i: vote(i))
    button.image = photo
    button.pack()

    label = Label(root, text=candidate['name'])
    label.pack()

# Create the show results button
show_results_button = Button(root, text="Note  ----  Click only the picture to select",
                             font= ('Helvica 20 bold italic'), height= 5, width= 60,command=show_results)
show_results_button.pack()

# Start the GUI event loop
root.mainloop()

