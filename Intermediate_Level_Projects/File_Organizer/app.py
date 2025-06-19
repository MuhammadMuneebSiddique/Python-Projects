import os
import shutil
import streamlit as st

st.title("File Organizer 📝")
path = st.text_input("Enter the Path of Folder: ")

category = {}

if st.button("Submit"):
    user_data = os.listdir(path)

    for items in user_data:
        if os.path.splitext(items)[1].lower() in [".jpg", ".jpeg", ".png", ".gif"]:
            category["images"] = []
        elif os.path.splitext(items)[1].lower() in [".pdf", ".docx", ".txt", ".xlsx"]:
            category["documents"] = []
        elif os.path.splitext(items)[1].lower() in [".mp4", ".avi", ".mov"]:
            category["videos"] = []
        elif os.path.splitext(items)[1].lower() in [".mp3", ".wav"]:
            category["music"] = []
        elif not os.path.isdir(f"{path}\{items}"):
            category["other"] = []


    for items in user_data:
        if os.path.splitext(items)[1].lower() in [".jpg", ".jpeg", ".png", ".gif"]:
            category["images"].append(items)
        elif os.path.splitext(items)[1].lower() in [".pdf", ".docx", ".txt", ".xlsx"]:
            category["documents"].append(items)
        elif os.path.splitext(items)[1].lower() in [".mp4", ".avi", ".mov"]:
            category["videos"].append(items)
        elif os.path.splitext(items)[1].lower() in [".mp3", ".wav"]:
            category["music"].append(items)
        elif not os.path.isdir(f"{path}\{items}"):
            category["other"].append(items)

    with st.expander("File Schema"):
        st.write(category)

    # Images
    if category["images"]:
        if os.path.exists(path+r"\images"):
            for items in category["images"]:
                shutil.move(path+f"\{items}",path+r"\images"+f"\{items}")
                # shutil.move(path+f"\{items}",fr"C:\Users\LENOVO\Downloads\{items}")
            st.success("Successfully Transfer Image Files in Image Folder")
            print(f"Successfully Transfer Image Files {len(category['images'])}")
        else:
            os.mkdir(path+r"\images")
            for items in category["images"]:
                shutil.move(path+f"\{items}",path+r"\images"+f"\{items}")
            
                # shutil.move(path+f"\{items}",fr"C:\Users\LENOVO\Downloads\{items}")
            st.success("Successfully Transfer Image Files in Image Folder")
            print(f"Successfully Transfer Image Files {len(category['images'])}")

    # documents
    if category["documents"]:
        if os.path.exists(path+r"\documents"):
            for items in category["documents"]:
                shutil.move(path+f"\{items}",path+r"\documents"+f"\{items}")
                # shutil.move(path+f"\{items}",fr"C:\Users\LENOVO\Downloads\{items}")
            st.success("Successfully Transfer Document Files in Document Folder")
            print("Successfully Transfer Document Files")
        else:
            os.mkdir(path+r"\documents")
            for items in category["documents"]:
                shutil.move(path+f"\{items}",path+r"\documents"+f"\{items}")
                # shutil.move(path+f"\{items}",fr"C:\Users\LENOVO\Downloads\{items}")
            st.success("Successfully Transfer Document Files in Document Folder")
            print("Successfully Transfer Document Files")

    # videos
    if "videos" in category:
        if os.path.exists(path+r"\videos"):
            for items in category["videos"]:
                shutil.move(path+f"\{items}",path+r"\videos"+f"\{items}")
                # shutil.move(path+f"\{items}",fr"C:\Users\LENOVO\Downloads\{items}")
            st.success("Successfully Transfer Video Files in Video Folder")
            print("Successfully Transfer Video Files")
        else:
            os.mkdir(path+r"\videos")
            for items in category["videos"]:
                shutil.move(path+f"\{items}",path+r"\videos"+f"\{items}")
                # shutil.move(path+f"\{items}",fr"C:\Users\LENOVO\Downloads\{items}")
            st.success("Successfully Transfer Video Files in Video Folder")
            print("Successfully Transfer Video Files")

    # music
    if "musics" in category:
        if os.path.exists(path+r"\musics"):
            for items in category["musics"]:
                shutil.move(path+f"\{items}",path+r"\musics"+f"\{items}")
                # shutil.move(path+f"\{items}",fr"C:\Users\LENOVO\Downloads\{items}")
            st.success("Successfully Transfer Music Files in Music Folder")
            print("Successfully Transfer Music Files")
        else:
            os.mkdir(path+r"\musics")
            for items in category["musics"]:
                shutil.move(path+f"\{items}",path+r"\musics"+f"\{items}")
                # shutil.move(path+f"\{items}",fr"C:\Users\LENOVO\Downloads\{items}")
            st.success("Successfully Transfer Music Files in Music Folder")
            print("Successfully Transfer Music Files")

    # other
    if category["other"]:
        if os.path.exists(path+r"\other"):
            for items in category["other"]:
                shutil.move(path+f"\{items}",path+r"\other"+f"\{items}")
                # shutil.move(path+f"\{items}",fr"C:\Users\LENOVO\Downloads\{items}")
            st.success("Successfully Transfer Other Files in Other Folder")
            print("Successfully Transfer other Files")
        else:
            os.mkdir(path+r"\other")
            for items in category["other"]:
                shutil.move(path+f"\{items}",path+r"\other"+f"\{items}")
                # shutil.move(path+f"\{items}",fr"C:\Users\LENOVO\Downloads\{items}")
            st.success("Successfully Transfer Other Files in Other Folder")
            print("Successfully Transfer other Files")
