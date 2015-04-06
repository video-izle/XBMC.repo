# -*- coding: utf-8 -*-
# please visit 

import xbmc,xbmcgui,xbmcplugin,sys
icons = xbmc.translatePath("special://home/addons/plugin.video.TURKizle/resources/icons/")
icon = xbmc.translatePath("special://home/addons/plugin.video.TURKizle/icon.png")
plugin_handle = int(sys.argv[1])
mode = sys.argv[2]

	
def ginico(url):
    import resources.lib.requests as requests

    if 'xxx&User' in url:
        x = url.partition('xxx&User')
        url = x[0] + 'xxx'
    x = url.partition('---')
    url = x[0]
    id = x[2].replace('xxx','')

    r = requests.get("http://giniko.com/watch.php?id=" + id)
    if r.text.find('m3u8?'):
        s = r.text.partition('m3u8?')
        s = s[2].partition('"')
        if len(s[0]) > 120 and len(s[0]) < 134:
            s = url + '?' + s[0]
            return s
    r = requests.get("http://giniko.com/watch.php?id=37")
    if r.text.find('m3u8?'):
        s = r.text.partition('m3u8?')
        s = s[2].partition('"')
        if len(s[0]) > 120 and len(s[0]) < 134:
            s = url + '?' + s[0]
            return s
    r = requests.get("http://giniko.com/watch.php?id=220")
    if r.text.find('m3u8?'):
        s = r.text.partition('m3u8?')
        s = s[2].partition('"')
        if len(s[0]) > 120 and len(s[0]) < 134:
            s = url + '?' + s[0]
            return s
    else: return url
	
def add_video_item(url, infolabels, img=''):
    url = 'plugin://plugin.video.TURKizle/?oynat=' + url + '***' + infolabels['title'] + '***' + img
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty('IsPlayable', 'false')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem)
    return
	
def playginico():
    xbmcPlayer = xbmc.Player()
    idx = mode.replace("?oynat=", "").replace("###", "|").replace("#x#", "?").replace("#h#", "http://").split('***')
    xbmc.executebuiltin('XBMC.Notification('+idx[1]+' , Kanal yükleniyor... ,5000,'+idx[2]+')')
    listitem = xbmcgui.ListItem( idx[1], iconImage=idx[2], thumbnailImage=idx[2])
    playlist = xbmc.PlayList( xbmc.PLAYLIST_VIDEO )
    playlist.clear()
    if 'giniko' in idx[0]: url = ginico(idx[0])
    else: url = idx[0]
    playlist.add( url, listitem )
    xbmcPlayer.play(playlist,None,False)
    sys.exit(0)

def main():
    add_video_item('http://origin.live.web.tv.streamprovider.net/streams/7acfc999bbde179fc45f18506125345f_live_0_0/index.m3u8',{ 'title': 'Star TV'}, icons + '83.png')
    add_video_item('http://mn-l.mncdn.com/showtv/showtv2/playlist.m3u8',{ 'title': 'Show TV'}, icons + '96.png')
    add_video_item('http://yayin5.canlitv.com:1935/live/foxtv/BratuMarian.m3u8',{ 'title': 'Fox TV'}, icons + '195.png')
    add_video_item('http://hls01-03.az.myvideo.az/hls-live/livepkgr/tv8/tv8/tv8.m3u8?seyirturk=fb:simpletvipadresleri3',{ 'title': 'TV 8'}, icons + 'tv8.png')
    add_video_item('http://212.224.108.80/S1/HLS_LIVE/kanald/1500/prog_index.m3u8',{ 'title': 'Kanal D'}, icons + '85.png')
    add_video_item('http://hls01-01.az.myvideo.az/hls-live/livepkgr/atvturk/atvturk/atvturk.m3u8?seyirturk=fb:simpletvipadresleri3',{ 'title': 'ATV'}, icons + '98.png')
    add_video_item('http://hls.turkuvazgroup.net:1935/minikacocuk/minikacocuk3/playlist.m3u8',{ 'title': 'minica Cocuc'}, icons + 'minika.png')
    add_video_item('http://trtcanlitv-lh.akamaihd.net/i/TRTHD_1@182045/master.m3u8',{ 'title': 'TRT'}, icons + '101.png')
    add_video_item('http://trtcanlitv-lh.akamaihd.net/i/TRT1HD_1@181842/master.m3u8',{ 'title': 'TRT 1'}, icons + '13.png')
    add_video_item('http://trtcanlitv-lh.akamaihd.net/i/TRT6_1@181944/master.m3u8',{ 'title': 'TRT 6'}, icons + '006.png')
    add_video_item('http://trtcanlitv-lh.akamaihd.net/i/TRTTURK_1@182144/master.m3u8',{ 'title': 'TRT Turk'}, icons + '51.png')
    add_video_item('http://trtcanlitv-lh.akamaihd.net/i/TRTCOCUK_1@181844/master.m3u8',{ 'title': 'TRT Cocuc'}, icons + '50.png')
    add_video_item('http://trtcanlitv-lh.akamaihd.net/i/TRTBELGESEL_1@182145/master.m3u8',{ 'title': 'TRT Belgesel'}, icons + '002.png')
    add_video_item('http://trtcanlitv-lh.akamaihd.net/i/TRTHABERHD_1@181942/master.m3u8',{ 'title': 'TRT Haber'}, icons + '196.png')
    add_video_item('http://trtcanlitv-lh.akamaihd.net/i/TRTMUZIK_1@181845/master.m3u8',{ 'title': 'TRT Muzik'}, icons + '49.png')
    add_video_item('http://trtcanlitv-lh.akamaihd.net/i/TRTSPOR1_1@182042/master.m3u8',{ 'title': 'TRT Spor'}, icons + '194.png')
    add_video_item('http://meclistv-lh.akamaihd.net/i/event_1@190503/master.m3u8',{ 'title': 'TRT 3 TBMM'}, icons + 'tr1.png')
    add_video_item('http://trtcanlitv-lh.akamaihd.net/i/TRTAVAZ_1@182244/master.m3u8',{ 'title': 'TRT Avaz'}, icons + 'tr2.png')
    add_video_item('http://trtcanlitv-lh.akamaihd.net/i/TRTOKUL_1@182245/master.m3u8',{ 'title': 'TRT Okul'}, icons + 'tr3.png')
    add_video_item('http://trtcanlitv-lh.akamaihd.net/i/TRTARAPCA_1@181945/master.m3u8',{ 'title': 'TRT Arapca'}, icons + 'tr4.png')
    add_video_item('http://trtcanlitv-lh.akamaihd.net/i/TRTDIYANET_1@182344/master.m3u8',{ 'title': 'TRT Diyanet'}, icons + 'tr5.png')
    add_video_item('rtmp://edge04-08.az.myvideo.az/dvrh264/canlintv/ playpath=mp4:canlintv swfUrl=http://www.myvideo.az/dvr/dvrManual4.swf live=1 pageUrl=http://www.myvideo.az',{ 'title': 'NTV'}, icons + '131.png')
    add_video_item('rtmp://edge03-08.az.myvideo.az/dvrh264/ntvspor/mp4:ntvspor swfUrl=http://www.myvideo.az/dvr/dvrManual4.swf live=1 pageUrl=http://www.myvideo.az',{ 'title': 'NTV Spor'}, icons + '132.png')

    add_video_item('http://yayin5.canlitv.com:1935/live/foxtv/BratuMarian.m3u8',{ 'title': 'Fox Turk'}, icons + '195.png')
    add_video_item('http://trtcanlitv-lh.akamaihd.net/i/TRTSPOR1_1@182042/master.m3u8',{ 'title': ' TRTSPOR HD '}, icons + '1.png')
    add_video_item('http://origin2.live.web.tv.streamprovider.net/streams/a6784af7d08a9c91dbfa0e4eab17e3bf_live_0_0/index.m3u8',{ 'title': ' A SPOR '}, icons + '1.png')	
    add_video_item('http://hls01-08.az.myvideo.az/hls-live/livepkgr/canlintv/canlintv/canlintv.m3u8?seyirturk=fb:simpletvipadresleri3',{ 'title': ' NTV '}, icons + '1.png')
    add_video_item('http://212.224.108.80/S1/HLS_LIVE/cnn_turk/1000/prog_index.m3u8',{ 'title': ' CNNTURK HD '}, icons + '1.png')	
    add_video_item('http://hd.yayin3.canlitv.mobi:7777/AHaber_HD/AHaber_High.m3u8',{ 'title': ' A HABER HD '}, icons + '1.png')	
    add_video_item('http://hls01-08.az.myvideo.az/hls-live/livepkgr/skyturk/skyturk/skyturk.m3u8?seyirturk=fb:simpletvipadresleri3',{ 'title': ' 360 '}, icons + '1.png')
    add_video_item('rtmp://tgrthaber.mediatriple.net:1935/tgrtliveedge/tgrt3',{ 'title': ' TGRT HABER '}, icons + '1.png')
    add_video_item('http://mn-l.mncdn.com/kanal24/kanal243/radyodelisi.m3u8',{ 'title': ' 24 TV '}, icons + '1.png')
    add_video_item('http://livetr.gostream.nl/ulketvhq/ulketvhq/hasbahca.m3u8',{ 'title': ' ULKE TV HD '}, icons + '1.png')
    add_video_item('http://canli.tvnet.tv.tr/hls-live/tvnet/_definst_/liveevent/livestream.m3u8',{ 'title': ' TV NET '}, icons + '1.png')	
    add_video_item('http://cine5.mobil.cubecdn.net/cine5/stream_1.m3u8',{ 'title': ' CINE5 '}, icons + '1.png')	
    add_video_item('http://sol.trtcdn.com/tv/trtdiyanet/smil:trtdiyanet.smil/hasbahca.m3u8 ',{ 'title': ' TRT DIYANET '}, icons + '1.png')
    add_video_item('http://livetr.gostream.nl/mekke/mekke/hasbahca.m3u8 ',{ 'title': ' KABE TV '}, icons + '1.png')
    add_video_item('http://livetr.gostream.nl/medine/medine/hasbahca.m3u8 ',{ 'title': ' MEDINE TV '}, icons + '1.png')
    add_video_item(' rtmp://sol.trtcdn.com/tv/trtarapca/mp4:trtarapca_3 ',{ 'title': ' TRT ARAPCA '}, icons + '1.png')
    add_video_item(' rtmp://yayin.dosttv.com/dosttv/dosttv2 ',{ 'title': ' DOST TV '}, icons + '1.png')
    add_video_item('http://semerkandglb.mediatriple.net:1935/semerkandliveedge/semerkand1/Playlist.m3u8 ',{ 'title': ' SEMERKAND HD '}, icons + '1.png')
    add_video_item('http://yayin8.canliyayin.org:1935/hilaltv/hilaltv/HasBahCa.m3u8 ',{ 'title': ' HILAL TV '}, icons + '1.png')	
    add_video_item('mms://yayin7.canliyayin.org/sinema',{ 'title': 'Sinema 1'}, icon)
    add_video_item('mms://yayin7.canliyayin.org/sinema1',{ 'title': 'Sinema 2'}, icon)
    add_video_item('mms://yayin7.canliyayin.org/sinema2',{ 'title': 'Sinema 3'}, icon)
    add_video_item('mms://yayin7.canliyayin.org/sinema3',{ 'title': 'Sinema 4'}, icon)
    add_video_item('mms://yayin7.canliyayin.org/sinema4',{ 'title': 'Sinema 5'}, icon)
    add_video_item('mms://yayin7.canliyayin.org/sinema5',{ 'title': 'Sinema 6'}, icon)
    add_video_item('mms://yayin7.canliyayin.org/sinema6',{ 'title': 'Sinema 7'}, icon)
    add_video_item('mms://yayin7.canliyayin.org/sinematurk',{ 'title': 'Sinema 8'}, icon)
    add_video_item('http://212.224.108.80/S1/HLS_LIVE/kanald/1500/prog_index.m3u8',{ 'title': ' KANALD HD '}, icons + '1.png')
    add_video_item('http://hd.yayin3.canlitv.mobi:7777/FoxTurkiye_HD/FoxTurkiye_High.m3u8',{ 'title': ' FOX TV HD '}, icons + '1.png')
    add_video_item('http://livetr.gostream.nl/kanal7hq/kanal7hq/chunklist_w1106540671.m3u8',{ 'title': ' KANAL7 HD '}, icons + '1.png')
    add_video_item('http://hls01-08.az.myvideo.az/hls-live/livepkgr/ntvspor/ntvspor/ntvspor.m3u8?seyirturk=fb:simpletvipadresleri3 ',{ 'title': ' NTV SPOR '}, icons + '1.png')
	




    xbmcplugin.endOfDirectory(plugin_handle)

if 'oynat' in mode:
    playginico()
else:
    main()