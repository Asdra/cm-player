Carte mère player-----------------
Url     : http://codes-sources.commentcamarche.net/source/36536-carte-mere-playerAuteur  : z_MurfDate    : 19/08/2013
Licence :
=========

Ce document intitulé « Carte mère player » issu de CommentCaMarche
(codes-sources.commentcamarche.net) est mis à disposition sous les termes de
la licence Creative Commons. Vous pouvez copier, modifier des copies de cette
source, dans les conditions fixées par la licence, tant que cette note
apparaît clairement.

Description :
=============

Sorte de 'piano' avec les buz de la carte m&egrave;re
<br /><a name='source-exe
mple'></a><h2> Source / Exemple : </h2>
<br /><pre class='code' data-mode='bas
ic'>
#L'essentiel du code: (sans la creation d'interface) :

#Lors d'un click
 sur le bouton 1:
def OnButton1Button(self, event):
#On appelle la fonction bu
z (prealablement importée de buz.py) :
    buz(1)
    event.Skip()

#La fonc
tion buz :
def buz(a):
#On charge la dll (necessite ctypes):
    buz = cdll.l
oad(&quot;sysbeuz.dll&quot;)
#si on a appelle le buz 1 (cette structure conditi
onnelle est repetee 16 fois):
    if a==1 :
#on dis a la dll de jouer le son N
°1
        buz.music1()

#Voila
</pre>
<br /><a name='conclusion'></a><h2> 
Conclusion : </h2>
<br />Cette applicatione necessite:
<br />WXPython ( <a hr
ef='http://wxpython.org' target='_blank'>http://wxpython.org</a> )
<br />Ctypes
 ( <a href='http://sourceforge.net/projects/ctypes/' target='_blank'>http://sour
ceforge.net/projects/ctypes/</a> )
<br />Sysbeuz.dll (inclue dans le zip, laiss
ez la dans le meme dossier que les autres fichiers.
<br />
<br />#############
##############################################
<br />#                         
                                #
<br /># Dezippez tout dans le meme fichier pu
is lancez App1.py  #
<br />#                                                   
      #
<br />###########################################################
<br 
/>
<br />Surprise : essayez de double cliquer sur l'image !!
<br />
<br />Ver
sion beta, la prochaine version devrait contenir ces modifications :
<br />-Les
 sons seront class&eacute;s selon la gamme
<br />-Un systeme de composition dir
ecte
<br />-Un systeme d'enregistrement
<br />
<br />Peut etre plus tard (si 
il y a une V2) :
<br />-un systeme de partage sur internet de vos creations
<b
r />-un petit jeux (style dance avec des fleches (mario dance mix))
