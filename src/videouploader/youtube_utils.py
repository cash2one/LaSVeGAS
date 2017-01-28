import subprocess

######
#
# The class is the wrapper over google's youtube_video_uploader.py which supports video upload functionality on youtube
# Upload video example: 
# python youtube_video_uploader.py --title 'test' --description 'valid description of the video' --file  final_output.mp4
# Before running point CLIENT_SECRETS_FILE to valid 'client_secrets.json'
#
#####


def constructVidProps(key, value):
	title = key
	desc = value
	category = '''22'''
	tags = key + ', wikipedia, meaning'
	return (title, desc, category, tags)


def UploadVideo(key, value, output_path, privacyStatus='public'):
	title, desc, category, tags = constructVidProps(key, value)
	upload_cmd = ("python src/videouploader/youtube_video_uploader.py "
								" --title '" + str(title) + "'"
								" --description '" + str(desc) + "'"
								" --category '" + str(category) + "'"
								" --keywords '" + str(tags) + "'"
								" --file '" + str(output_path) + "'"
								" --privacyStatus '" + str(privacyStatus)) +  "'"
	subprocess.call(upload_cmd, shell=True)
