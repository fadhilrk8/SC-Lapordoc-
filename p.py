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
        self.root.title("LAPORDOC!")

        # Data dokter
        self.doctors = [
            Doctor("dr. Agung, Sp.M", "Mata", "082145678901", "09:00-12:00, Jumat: 09:00-11:30, Sabtu: 12:00-15:00"),
            Doctor("dr. Adrian, Sp.M", "Mata", "081234567890", "Senin: 09:00-12:00, Rabu: 12:00-15:00"),
            Doctor("dr. Cessy, Sp.M", "Mata", "08567890234", "Minggu: 09:00-12:00, Kamis: 12:00-15:00"),
            Doctor("drg. Agnesia", "Gigi", "089789012345", "Senin: 09:00-12:00, Rabu: 12:00-15:00"),
            Doctor("drg. Fendly", "Gigi", "081234567891", "Selasa: 09:00-12:00, Jumat: 12:00-15:00, Sabtu: 09:00-11.30"),
            Doctor("drg. Nadila", "Gigi", "082145678902", "Minggu: 09:00-11:30, Kamis: 09:00-12:00"),
            Doctor("dr. Chandra, Sp.KK", "Luar tubuh", "0856789012345", "Senin: 09:00-12:00, Rabu: 12:00-15:00"),
            Doctor("dr. Rafika, Sp.DV", "Luar tubuh", "0897890123456", "Selasa: 09:00-12:00, Jumat: 09:00-11:45, Sabtu: 09:00-11:30"),
            Doctor("dr. Parwoto, Sp.KK", "Luar tubuh", "081234567892", "Minggu: 12:00-15:00, Kamis: 09:00-12:00"),
            Doctor("dr. Pratama Sp.PD", "Dalam tubuh", "082145678903", "Senin: 09:00-12:00, Rabu: 12:00-15:00"),
            Doctor("dr. Iskandar Sp.PD", "Dalam tubuh", "085678901236", "Selasa: 09:00-12:00, Jumat: 09:00-11:30, Sabtu:09:00-11:45"),
            Doctor("dr. Theresia Sp.PA", "Dalam tubuh", "089789012347", "Minggu: 09:00-12:00, Kamis: 12:00-15:00"),
            Doctor("dr. Hayulani, Sp.KJ", "Jiwa", "081234567893", "Senin: 09:00-12:00, Rabu: 09:00-11:30"),
            Doctor("dr. Belinda, Sp.Psi.,M.Psi", "Jiwa", "082145678904", "Selasa: 09:00-12:00, Jumat: 09:00-11:30, Sabtu: 12:00-14:00"),
            Doctor("dr. Elissa, Sp.KJ", "Jiwa", "085678901237", "Minggu: 09:00-12:00, Kamis: 09:00-12:00"),
            Doctor("dr. Mega, Sp.THT-KL", "THT", "08125543678", " Senin: 09:00-12:00, Rabu: 09:00-11:30"),
            Doctor("dr. Wicak, Sp.THTBKL", "THT", "089673172258", "Selasa: 09:00-12:00, Jumat: 09:00-11:30"),
            Doctor("dr. Rinindra, Sp.THT", "THT", "081329972375", "Sabtu: 15:30-16:30, Minggu: 11:30-12:00, Kamis: 13:00-15:00"),
        ]

        # Widget Tkinter
        self.specialization_label = tk.Label(root, text="Pilih Spesialisasi Dokter:", font=("Helvetica", 10, "bold"))
        self.specialization_label.grid(row=0, column=0, pady=10)

        self.specialization_var = tk.StringVar(root)
        self.specialization_var.set("Mata")  # Spesialisasi default
        self.specialization_menu = tk.OptionMenu(root, self.specialization_var, "Mata", "Gigi", "Luar tubuh", "Dalam tubuh", "Jiwa", "THT")
        self.specialization_menu.grid(row=0, column=1, pady=10)

        self.select_button = tk.Button(root, text="Pilih Dokter", command=self.show_doctor_info)
        self.select_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.doctor_listbox = tk.Listbox(root, width=30, selectmode=tk.SINGLE)
        self.doctor_listbox.grid(row=2, column=0, columnspan=2, pady=10,)

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
            selected_index = int(simpledialog.askstring("Pilih Dokter", "Pilih nomor dokter:")) # type: ignore
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