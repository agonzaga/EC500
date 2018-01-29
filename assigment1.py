from google.cloud import videointelligence
import io, os
import tweepy
import wget



# Twitter
#----------------------------------------------------------------------------------------------------# 

# Consumer Information
consumer_key = 'NONE'
consumer_secret = 'NONE'
access_token = 'NONE'
access_secret = 'NONE'
 
# Authorization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
DIRECTORY = os.getcwd()

# Gather data from this twitter name
twitter_handle = 'realdonaldtrump' 

# Gathering twitter data
try:
    tweets = api.user_timeline(screen_name=twitter_handle,          # Gather first set of tweets
                           count=50, include_rts=False,
                           exclude_replies=True)
except:
    twitter_handle = input('The given username does not exist \n')

max_id = tweets[-1].id


# Traversing tweets and finding those with images
media_files = set()
for status in tweets:
    media = status.entities.get('media', [])
    if(len(media) > 0):
        media_files.add(media[0]['media_url'])

# Downloading images
for media_file in media_files:
    wget.download(media_file)



#FFMPEG
#-----------------------------------------------------------------------------------------------------#
# Converting all images that were downloaded into a single video file
os.system('cat *.jpg | ffmpeg -f image2pipe -framerate .5 -i - output.mp4')



#Google NOT WORKING
#-----------------------------------------------------------------------------------------------------#
video_client = videointelligence.VideoIntelligenceServiceClient()
features = [videointelligence.enums.Feature.LABEL_DETECTION]

with io.open('output.mp4', 'rb') as movie:
    input_content = movie.read()

operation = video_client.annotate_video(features=features, input_content=input_content)
print('\nProcessing video for label annotations:')

result = operation.result(timeout=90)
print('\nFinished processing.')


frame_labels = result.annotation_results[0].frame_label_annotations
for i, frame_label in enumerate(frame_labels):
    print('Frame label description: {}'.format(frame_label.entity.description))
    for category_entity in frame_label.category_entities:
        print('\tLabel category description: {}'.format(category_entity.description))





