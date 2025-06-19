import streamlit as st
import os
import json
import hashlib 

def Load_file(filename):
    if os.path.exists(filename):
        with open(filename,"r") as file:
            return json.load(file)
    else:
        return {}

def save_file_data(filename,data):
    with open(filename,"w")as file:
        json.dump(data,file)

def passward(user_passward):
    return hashlib.sha256(user_passward.encode()).hexdigest()

user = Load_file("user.json")
data = Load_file("data.json")


# ----------------- STATE SETUP ------------------ #
if "user" not in st.session_state:
    st.session_state.user = None

menu = ["Home","Add Expense"]
if st.session_state.user:
    menu += ["View Expense","Edit & Delete Expense","Logout"]
else:
    menu += ["Login","Sign Up"]
choice = st.sidebar.radio("Navigation",menu)

# Sign Up
if choice == "Sign Up":
    st.subheader("Create a New Account")
    user_name = st.text_input("User Name")
    email = st.text_input("Email")
    user_passward = st.text_input("Passward")
    if st.button("sign up"):
        if user_name not in user.keys():
            if user_name and user_passward:
                if "@" in email:
                    user_details = {
                        "username":user_name,
                        "email":email,
                        "passward":passward(user_passward)
                    }
                    user[user_name] = user_details
                    save_file_data("user.json",user)
                    st.success("Account Created Successfully")
            else:
                st.error("Please enter the correct name or passward")
        else:
            st.error("user name is already exist")

# Login 
if choice == "Login":
    st.subheader("LOGIN")
    user_name = st.text_input("User Name")
    email = st.text_input("Email")
    user_passward = st.text_input("Passward")
    if st.button("Log in"):
        if user_name == user[user_name]["username"]:
            if email == user[user_name]["email"]:
                if passward(user_passward) == user[user_name]["passward"]:
                    st.session_state.user = user_name
                    st.success("Login Successfully")
                else:
                    st.error("Incorrect Passward")
            else:
                st.error("Incorrect Email")
        else:
            st.error("Incorrect User Name")

# Add Expense
if choice == "Add Expense":
    st.subheader("Add Expense")
    amount = st.text_input("Enter the amount of Expence")
    category = st.text_input("Enter the Category of Expence")
    optional_notes = st.text_area("Enter the notes")
    date = st.date_input("Date")
    if st.button("Add"):
        st.write(date)
        if st.session_state.user in data.keys():
            if amount:
                if category:
                    if date:
                        expense = data[st.session_state.user]
                        expense.append({"amount":amount,"category":category,"optional_notes":optional_notes,"date":f"{date}"})        
                        data[st.session_state.user] = expense
                        save_file_data("data.json",data)
                        st.success("Expense Add Successfully")
                    else:
                        st.error("Please enter the Date")
                else:
                    st.error("Please enter the Category")
            else:
                st.error("Please enter the Amount")
        else:  
            if amount:
                if category:
                    if date:
                        expense = []
                        expense.append({"amount":amount,"category":category,"optional_notes":optional_notes,"date":f"{date}"})        
                        data[st.session_state.user] = expense
                        save_file_data("data.json",data)
                        st.success("Expense Add Successfully")
                    else:
                        st.error("Please enter the Date")
                else:
                    st.error("Please enter the Category")
            else:
                st.error("Please enter the Amount")

# View Expence
if choice == "View Expense":
    st.subheader("View Expense")
    if st.session_state.user in data.keys():
        for item in data[st.session_state.user]:
            with st.expander(f"Expence Category:  {item["category"].capitalize()}"):
                st.write(f"Amount:  {item["amount"]}")
                if item["optional_notes"]:
                    st.write(f"Notes:  {item["optional_notes"]}")
                st.write(f"Date:  {item["date"]}")
    else:
        st.write("No Expense")


# Delete Expense 
if choice == "Edit & Delete Expense":
    st.subheader("Edit & Delete Expense")
    if st.session_state.user in data.keys():
        if data[st.session_state.user] != []:
            for item in data[st.session_state.user]:
                with st.expander(f"Expense Name: {item["category"]}"):
                    new_amount = st.text_input("Amount",value=item["amount"])
                    new_category = st.text_input("Category",value=item["category"])
                    new_notes = st.text_input("Notes",value=item["optional_notes"])
                    new_date = st.date_input("Date",value=item["date"])
                    if st.button("Save"):
                        item["amount"] = new_amount
                        item["category"] = new_category
                        item["optional_notes"] = new_notes
                        item["date"] = f"{new_date}"
                        save_file_data("data.json",data)
                        st.success("Updated Successfully")
                    if st.button("Delete"):
                        data[st.session_state.user].remove(item)
                        save_file_data("data.json",data)
                        st.success("Remove Successfully")
        else:
            st.write("No Expense")


# logout 
if choice == "Logout":
    st.title("Logout")
    st.write("Click here to logout")
    if st.button("Logout"):
        st.session_state.user = None


