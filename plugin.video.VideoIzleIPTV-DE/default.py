# -*- coding: utf-8 -*-
# please visit http://www.iptvxtra.net

import xbmc,xbmcgui,xbmcplugin,sys
icons = xbmc.translatePath("special://home/addons/plugin.video.iptvxtra-trtv/resources/icons/")
icon = xbmc.translatePath("special://home/addons/plugin.video.iptvxtra-trtv/icon.png")
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
    url = 'plugin://plugin.video.iptvxtra-trtv/?playtrk=' + url + '***' + infolabels['title'] + '***' + img
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty('IsPlayable', 'false')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem)
    return
	
def playginico():
    xbmcPlayer = xbmc.Player()
    idx = mode.replace("?playtrk=", "").replace("###", "|").replace("#x#", "?").replace("#h#", "http://").split('***')
    xbmc.executebuiltin('XBMC.Notification('+idx[1]+' , einen Moment der Sender wird geladen ,5000,'+idx[2]+')')
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
    add_video_item('http://hd.yayin3.canlitv.mobi:7777/ShowTV_HD/ShowTV_High.m3u8',{ 'title': 'Show TV'}, icons + '96.png')
    add_video_item('http://hd.yayin3.canlitv.mobi:7777/FoxTurkiye_HD/FoxTurkiye_High.m3u8',{ 'title': 'Fox Turk'}, icons + '195.png')
    add_video_item('http://hd.yayin3.canlitv.mobi:7777/TV8_HD/TV8_High.m3u8',{ 'title': 'TV 8'}, icons + 'tv8.png')
    add_video_item('http://nimlive1.giniko.com/kanald/kanald.stream/playlist.m3u8---85xxx',{ 'title': 'Kanal D'}, icons + '85.png')
    add_video_item('http://nimlive1.giniko.com/atvtv/atvtvtv.stream/playlist.m3u8---98xxx',{ 'title': 'a TV'}, icons + '98.png')
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
    add_video_item('http://nimlive1.giniko.com/atlastv/atlastv.stream/playlist.m3u8---209xxx',{ 'title': 'Atlas Ordu TV'}, icons + '209.png')
    add_video_item('http://nimlive1.giniko.com/bursaas/bursaas.stream/playlist.m3u8---211xxx',{ 'title': 'Bursa AS TV'}, icons + '211.png')
    add_video_item('http://nimlive1.giniko.com/cnbce/cnbce.stream/playlist.m3u8---133xxx',{ 'title': 'CNBC-e'}, icons + '133.png')
    add_video_item('http://nimlive1.giniko.com/ebrutv/ebrutv.stream/playlist.m3u8---47xxx',{ 'title': 'Ebru TV'}, icons + '47.png')
    add_video_item('http://nimlive1.giniko.com/emtv1/emtv1.stream/playlist.m3u8---208xxx',{ 'title': 'EM TV'}, icons + '208.png')
    add_video_item('http://nimlive1.giniko.com/fbtv1/fb-tv.stream/playlist.m3u8---210xxx',{ 'title': 'FB TV'}, icons + '210.png')
    add_video_item('http://nimlive1.giniko.com/kanal7/kanal7.stream/playlist.m3u8---199xxx',{ 'title': 'Kanal 7'}, icons + '199.png')
    add_video_item('http://nimlive1.giniko.com/kraltv/kraltv.stream/playlist.m3u8---84xxx',{ 'title': 'Kral Pop'}, icons + '84.png')
    add_video_item('http://nimlive1.giniko.com/maxitv/maxitv.stream/playlist.m3u8---212xxx',{ 'title': 'Maxi TV'}, icons + '212.png')
    add_video_item('http://nimlive1.giniko.com/muzikturk/muzikturk.stream/playlist.m3u8---172xxx',{ 'title': 'Muzik Turk'}, icons + '172.png')
    add_video_item('http://nimlive1.giniko.com/sportstv/sportstv/playlist.m3u8---215xxx',{ 'title': 'Sports TV'}, icons + '215.png')
    add_video_item('http://nimlive1.giniko.com/planetc/planetc.stream/playlist.m3u8---175xxx',{ 'title': 'Planet Cocuk'}, icons + '175.png')
    add_video_item('http://nimlive1.giniko.com/planetm/planetm.stream/playlist.m3u8---177xxx',{ 'title': 'Planet Mutfak'}, icons + '177.png')
    add_video_item('http://nimlive1.giniko.com/planetp/planetp.stream/playlist.m3u8---176xxx',{ 'title': 'Planet Pembe'}, icons + '176.png')
    add_video_item('http://nimlive1.giniko.com/planett/planett.stream/playlist.m3u8---178xxx',{ 'title': 'Planet Turk'}, icons + '178.png')
    add_video_item('http://nimlive1.giniko.com/samanyolu/samanyolu.stream/playlist.m3u8---48xxx',{ 'title': 'Samanyolu TV'}, icons + '48.png')
    add_video_item('http://nimlive1.giniko.com/supertv/supertv.stream/playlist.m3u8---165xxx',{ 'title': 'Super TV'}, icons + '165.png')
    add_video_item('http://nimlive1.giniko.com/tmb_tv/tmb_tv.stream/playlist.m3u8---227xxx',{ 'title': 'Turk Muzik Birligi TV'}, icons + '227.png')
    add_video_item('http://nimlive1.giniko.com/tv2tv/tv_2tv.stream/playlist.m3u8---173xxx',{ 'title': 'TV 2'}, icons + '173.png')
    add_video_item('http://nimlive1.giniko.com/ulketv/ulketv.stream/playlist.m3u8---200xxx',{ 'title': 'Ulke TV'}, icons + '200.png')
    add_video_item('http://nimlive1.giniko.com/yurdumtv/yurdum.stream/playlist.m3u8---207xxx',{ 'title': 'Yurdum TV'}, icons + '207.png')
    add_video_item('http://nimlive1.giniko.com/worldtravel/worldtravel.stream/playlist.m3u8---198xxx',{ 'title': 'World Travel Channel'}, icons + '198.png')
    add_video_item('rtmp://edge04-08.az.myvideo.az/dvrh264/canlintv/ playpath=mp4:canlintv swfUrl=http://www.myvideo.az/dvr/dvrManual4.swf live=1 pageUrl=http://www.myvideo.az',{ 'title': 'NTV'}, icons + '131.png')
    add_video_item('rtmp://edge03-08.az.myvideo.az/dvrh264/ntvspor/mp4:ntvspor swfUrl=http://www.myvideo.az/dvr/dvrManual4.swf live=1 pageUrl=http://www.myvideo.az',{ 'title': 'NTV Spor'}, icons + '132.png')
    add_video_item('http://nimlive1.giniko.com/eurod/eurod.stream/playlist.m3u8---164xxx',{ 'title': 'Euro D'}, icons + '164.png')
    # add_video_item('http://yayin5.canlitv.com:1935/live/foxtv/BratuMarian.m3u8',{ 'title': 'Fox Turk'}, icons + '195.png')
    # add_video_item('http://nimlive1.giniko.com/startv/startvge.stream/playlist.m3u8---83xxx',{ 'title': 'Star TV'}, icons + '83.png')
    # add_video_item('http://nimlive1.giniko.com/ntvtv/ntvlive.stream/playlist.m3u8---131xxx',{ 'title': 'NTV'}, icons + '131.png')
    # add_video_item('http://nimlive1.giniko.com/ntvspor/ntv-sport.stream/playlist.m3u8---132xxx',{ 'title': 'NTV Spor'}, icons + '132.png')

    add_video_item('mms://yayin7.canliyayin.org/sinema',{ 'title': 'Sinema 1'}, icon)
    add_video_item('mms://yayin7.canliyayin.org/sinema1',{ 'title': 'Sinema 2'}, icon)
    add_video_item('mms://yayin7.canliyayin.org/sinema2',{ 'title': 'Sinema 3'}, icon)
    add_video_item('mms://yayin7.canliyayin.org/sinema3',{ 'title': 'Sinema 4'}, icon)
    add_video_item('mms://yayin7.canliyayin.org/sinema4',{ 'title': 'Sinema 5'}, icon)
    add_video_item('mms://yayin7.canliyayin.org/sinema5',{ 'title': 'Sinema 6'}, icon)
    add_video_item('mms://yayin7.canliyayin.org/sinema6',{ 'title': 'Sinema 7'}, icon)
    add_video_item('mms://yayin7.canliyayin.org/sinematurk',{ 'title': 'Sinema 8'}, icon)







    xbmcplugin.endOfDirectory(plugin_handle)

if 'playtrk' in mode:
    playginico()
else:
    main()