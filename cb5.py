import tkinter as tk
from tkinter import messagebox, simpledialog

class Doctor:
    def __init__(self, name, specialization, phone, schedule):
        self.name = name
        self.specialization = specialization
        self.phone = phone
        self.schedule = schedule

class DoctorSelectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LAPORDOK!")

        # Data dokter
        self.doctors = [
            Doctor("Dr. John Doe", "Umum", "123-456-7890", "Senin - Jumat, 08:00 - 17:00"),
            Doctor("Dr. Jane Smith", "Umum", "987-654-3210", "Senin - Jumat, 09:00 - 18:00"),
            Doctor("Dr. Mark Johnson", "Umum", "111-222-3333", "Senin - Jumat, 10:00 - 19:00"),
            Doctor("Dr. Sarah Brown", "Gigi", "444-555-6666", "Senin - Jumat, 08:30 - 17:30"),
            Doctor("Dr. Michael White", "Gigi", "777-888-9999", "Senin - Jumat, 09:30 - 18:30"),
            Doctor("Dr. Emily Davis", "Gigi", "555-444-3333", "Senin - Jumat, 11:00 - 20:00"),
        ]

        # Widget Tkinter
        self.specialization_label = tk.Label(root, text="Pilih Spesialisasi Dokter:", font=("Helvetica", 10, "bold"))
        self.specialization_label.grid(row=0, column=0, pady=10)

        self.specialization_var = tk.StringVar(root)
        self.specialization_var.set("Umum")  # Spesialisasi default
        self.specialization_menu = tk.OptionMenu(root, self.specialization_var, "Umum", "Gigi")
        self.specialization_menu.grid(row=0, column=1, pady=10)

        self.select_button = tk.Button(root, text="Pilih Dokter", command=self.show_doctor_info)
        self.select_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.doctor_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.doctor_listbox.grid(row=2, column=0, columnspan=2, pady=10)

        self.doctor_info_frame = tk.Frame(root)
        self.doctor_info_label = tk.Label(self.doctor_info_frame, text="")
        self.doctor_info_label.pack(pady=10)

    def update_doctor_list(self):
        selected_specialization = self.specialization_var.get()
        selected_doctors = [doctor for doctor in self.doctors if doctor.specialization == selected_specialization]
        
        self.doctor_listbox.delete(0, tk.END)
        for i, doctor in enumerate(selected_doctors, start=1):
            self.doctor_listbox.insert(tk.END, f"{i}. {doctor.name}")

    def show_doctor_info(self):
        selected_specialization = self.specialization_var.get()
        selected_doctors = [doctor for doctor in self.doctors if doctor.specialization == selected_specialization]

        if not selected_doctors:
            messagebox.showinfo("Info", "Tidak ada dokter tersedia untuk spesialisasi ini.")
            return

        self.update_doctor_list()

        try:
            selected_index = int(simpledialog.askstring("Pilih Dokter", "Pilih nomor dokter:"))
            if 1 <= selected_index <= len(selected_doctors):
                chosen_doctor = selected_doctors[selected_index - 1]
                info_text = f"Nama: {chosen_doctor.name}\nSpesialisasi: {chosen_doctor.specialization}\nNomor Telepon: {chosen_doctor.phone}\nJadwal Praktek: {chosen_doctor.schedule}"
                self.doctor_info_label.config(text=info_text)

                # Menyembunyikan widget saat ini
                self.specialization_label.grid_forget()
                self.specialization_menu.grid_forget()
                self.select_button.grid_forget()
                self.doctor_listbox.grid_forget()

                # Menampilkan halaman baru dengan informasi dokter terpilih
                self.doctor_info_frame.grid(row=0, column=0, columnspan=2, pady=10)

            else:
                messagebox.showinfo("Info", "Nomor dokter tidak valid.")
        except ValueError:
            messagebox.showinfo("Info", "Masukkan nomor dokter yang valid.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DoctorSelectionApp(root)
    root.mainloop()
