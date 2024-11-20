# 📝 Django Form Project  

Welcome to the **Django Form Project**! This application demonstrates a user-friendly form submission process with validation, redirection, and email notification features. Built using **Django**, **HTML**, **CSS**, **JavaScript**, and **jQuery**, this project also integrates **MySQL** for backend data management.  

---

## 🌟 Project Features  

### 🌐 **Starting Page: `index.html`**  
- Input fields for:  
  - **Name**  
  - **Email**  
  - **Year**  
  - **USN** (University Serial Number)  
  - **Gender**  
  - A **checkbox** to accept terms and conditions.  
- Form validation to ensure proper data entry.  
- On submission, users are redirected to the **base.html** page.  

---

### 🔍 **Confirmation Page: `base.html`**  
- Displays the details entered by the user for review.  
- Users can:  
  - **Cross-check their input** for accuracy.  
  - Click the **Export** button to send their details via email for further verification.  

---

### 📧 **Email Notification**  
- Upon clicking **Export**, the entered details are sent to the user’s email.  
- Ensures the data entered is correct and provides an additional layer of verification.  

---

### ✅ **Final Page: `final.html`**  
- Displays a **Django HttpResponse** confirming:  
  > "Mail has been sent. Please check."  

---

## 🛠️ Technologies Used  

- **Django**: For backend logic and framework support.  
- **HTML & CSS**: For structuring and styling the pages.  
- **JavaScript & jQuery**: For interactive and dynamic elements.  
- **MySQL**: For database management.  

---

## 🚀 How to Run the Project Locally  

1. Clone the repository:  
   ```bash
   git clone <repository-url>
   cd <repository-folder>
