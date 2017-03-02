from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Album, Song


def index(request):
    all_albums = Album.objects.all()

    context = {
        'all_albums': all_albums,
    }
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(id=request.POST['song'])
    except (KeyError, Exception):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "YOu DUMPY DUMB. IT IS NOT A VALID SONG ID... whatever."
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
