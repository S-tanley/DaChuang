from test import get_img_from_camera_net

url = "rtsp://admin:miice520@192.168.200.23:554/Streaming/Channels/101" #211云台
folder_path = '/Users/zhengbowen/nondefault/DaChuang_local/output_video/213/'
get_img_from_camera_net(folder_path, url, 10*60, 50)
