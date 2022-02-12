



# I have already install pytube.

# from pytube import YouTube
 
# print("\nyoutube Playlist Downloder")
# URL=input("\nEnter youtube playlist url : ")
# playlist=YouTube(URL)
# Res=int(input("\nEnter video Quality : "))
# try:
#     print("\nplease wait....")
#     for video in YouTube(URL):
#        stream= video.streams.filter(file_extension="mp4").get_by_resolution(Res)
#        print(("\nDownloding : ",video.title))
#        stream.download()
#     print("\Downloading Success!")

# except:
#     print("\nSomthing went wrong!")
 











 # importing the module
from pytube import YouTube

# where to save
SAVE_PATH = "E:\youtube videos" #to_do

# link of the video to be downloaded
link=input("Enter The URL : ")

try:
	# object creation using YouTube
	# which was imported in the beginning
	yt = YouTube(link)
except:
	print("Connection Error") #to handle exception

# filters out all the files with "mp4" extension
mp4files = yt.filter('mp4')

#to set the name of the file
yt.set_filename('GeeksforGeeks Video')

# get the video with the extension and
# resolution passed in the get() function
d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
try:
	# downloading the video
	d_video.download(SAVE_PATH)
except:
	print("Some Error!")
print('Task Completed!')


