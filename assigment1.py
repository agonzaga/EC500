from google.cloud import videointelligence
import io, os
import tweepy
import wget


def module(twitter_handle, number_tweets):

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

    # Checking if there is already an output movie file
    os.system('rm output.mp4')
    

    # Gathering twitter data
    try:
        tweets = api.user_timeline(screen_name=twitter_handle,          # Gather first set of tweets
                               count=number_tweets, include_rts=False,
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

    result = operation.result()

    labels = []
    confidences = []
    segments = []

    segment_labels = result.annotation_results[0].segment_label_annotations
    for i, segment_label in enumerate(segment_labels):
        labels.append(segment_label.entity.description)

        for i, segment in enumerate(segment_label.segments):
            start_time = (segment.segment.start_time_offset.seconds +
                          segment.segment.start_time_offset.nanos / 1e9)
            end_time = (segment.segment.end_time_offset.seconds +
                        segment.segment.end_time_offset.nanos / 1e9)
            positions = '{}s to {}s'.format(start_time, end_time)
            confidences.append(segment.confidence)
            segments.append(positions)
        print('\n')

    print(labels)
    print(confidences)
    print(segments)

if __name__ == '__main__':
    module('realDonaldTrump', 100)

