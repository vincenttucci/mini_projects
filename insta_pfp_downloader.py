import instaloader
#downloads a user's instagram profile picture

profile_name = input("Enter Username Here: ")
print("Downloading Picture...")

L = instaloader.Instaloader()
L.download_profile(profile_name, profile_pic_only=True)

print("Download Complete.")
