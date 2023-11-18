import customtkinter
import getSpeech

def login():
    name = entry1.get()  # Get the text from entry1 (Name)
    email = entry2.get()  # Get the text from entry2 (Email)

    # Check if both Name and Email fields are not empty
    if name and email:
        root.withdraw()  # Hide the login window

        # Create a new window for the next page
        next_page = customtkinter.CTk()
        next_page.geometry("300x150")

        def record_data():
            print("Recording data...")
            # Add functionality to record data or navigate to another page
            
            getSpeech.main()

        record_button = customtkinter.CTkButton(master=next_page, text="Record", command=record_data)
        record_button.pack(pady=20)

        next_page.mainloop()
    else:
        print("Please enter both Name and Email.")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Name")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Email")
entry2.pack(pady=12, padx=10)

login_button = customtkinter.CTkButton(master=frame, text="Login", command=login)
login_button.pack(pady=12, padx=10)

root.mainloop()
