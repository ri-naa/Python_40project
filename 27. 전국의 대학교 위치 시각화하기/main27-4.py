import folium

map = folium.Map(location=[37,126],zoom_start=7)

marker = folium.Marker([37.560311827, 126.944695670], 
                       popup='이화여자대학교', 
                       icon = folium.Icon(color='green'))

marker.add_to(map)

map.save(r'27. 전국의 대학교 위치 시각화하기\map_ewha.html')