#!/usr/bin/python# -*- coding: utf-8 -*- import urllib,urllib2,re,xbmcplugin,xbmcgui,sys,xbmc,xbmcaddonimport osimport randomfrom xbmcaddon import Addon__settings__ = xbmcaddon.Addon(id='plugin.video.VideoIzleIPTV')__language__ = __settings__.getLocalizedStringhome = __settings__.getAddonInfo('path')icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )fanart = xbmc.translatePath( os.path.join( home, 'fanart.jpg' ) )folders = xbmc.translatePath(os.path.join(home, 'resources', 'lib'))sys.path.append(folders)xbmcPlayer = xbmc.Player()playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)def CATEGORIES():        tek='http://www.video-izle.tv/kodi/xml/TR.xml'        link=get_url(tek)        link=link.replace('&amp;','&')        match=re.compile('<title>(.*?)</title>\n<link>(.*?)</link>\n<thumbnail>(.*?)</thumbnail>').findall(link)        for name,url,t in match:                addLink('[COLOR lightblue]>> [/COLOR][COLOR lightgreen]'+ name+'[/COLOR]',url,t)                xbmc.executebuiltin('Container.SetViewMode(500)')#####youtube kontrol#######from xbmcaddon import Addon__YoutubePluginName__ = 'plugin.video.youtube'__YoutubeAddon__ = Addon(__YoutubePluginName__)youtubeVersion = __YoutubeAddon__.getAddonInfo('version')def Youtube_Player(url):        playList.clear()           code=re.match(r"http://www.youtube.com/embed/(.*?)$", url).group(1)        print '[code]'+str(code)        url='plugin://plugin.video.youtube/play/?video_id=' + code        name='MagicTR Reklam'        addLink(name,url,'')        playlist_yap(playList,name,url)        xbmcPlayer.play(playList)def Youtube_Player2(url):        playList.clear()           code=re.match(r"http://www.youtube.com/embed/(.*?)$", url).group(1)        print '[code]'+str(code)        url='plugin://plugin.video.youtube/?action=play_video&videoid=' + code        name='MagicTR Reklam'        addLink(name,url,'')        playlist_yap(playList,name,url)        xbmcPlayer.play(playList)        def playlist_yap(playList,name,url):        listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage="")        listitem.setInfo('video', {'name': name } )        playList.add(url,listitem=listitem)        return playList    def get_url(url):        req = urllib2.Request(url)        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')        response = urllib2.urlopen(req)        link=response.read()        response.close()        return linkdef addLink(name, url, thumbnail):    liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=thumbnail)    liz.setInfo(type="Video", infoLabels={"Title":name})    liz.setProperty("IsPlayable", "true")    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)def addDir(name,url,mode,iconimage):        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)        ok=True        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)        liz.setInfo( type="Video", infoLabels={ "Title": name } )        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)        return okdef get_params():        param=[]        paramstring=sys.argv[2]        if len(paramstring)>=2:                params=sys.argv[2]                cleanedparams=params.replace('?','')                if (params[len(params)-1]=='/'):                        params=params[0:len(params)-2]                pairsofparams=cleanedparams.split('&')                param={}                for i in range(len(pairsofparams)):                        splitparams={}                        splitparams=pairsofparams[i].split('=')                        if (len(splitparams))==2:                                param[splitparams[0]]=splitparams[1]                                        return param              params=get_params()url=Nonename=Nonemode=Nonetry:        url=urllib.unquote_plus(params["url"])except:        passtry:        name=urllib.unquote_plus(params["name"])except:        passtry:        mode=int(params["mode"])except:        passprint "Mode: "+str(mode)print "URL: "+str(url)print "Name: "+str(name)if mode==None or url==None or len(url)<1:        CATEGORIES()        xbmcplugin.endOfDirectory(int(sys.argv[1]))