from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from photo_objects.django import api
from photo_objects.django.api.utils import AlbumNotFound, FormValidationFailed
from photo_objects.django.forms import ModifyPhotoForm, UploadPhotosForm
from photo_objects.django.views.utils import BackLink, render_markdown

from .utils import json_problem_as_html


@json_problem_as_html
def upload_photos(request: HttpRequest, album_key: str):
    if request.method == "POST":
        try:
            api.upload_photos(request, album_key)
            return HttpResponseRedirect(
                reverse(
                    'photo_objects:show_album',
                    kwargs={"album_key": album_key}))
        except FormValidationFailed as e:
            form = e.form
    else:
        form = UploadPhotosForm()

    album = api.check_album_access(request, album_key)
    target = album.title or album.key
    back = BackLink(
        f"Back to {target}", reverse(
            'photo_objects:show_album', kwargs={
                "album_key": album_key}))

    return render(request, 'photo_objects/photo/upload.html', {
        "form": form,
        "title": "Upload photos",
        "back": back,
        "photo": album.cover_photo,
    })


@json_problem_as_html
def show_photo(request: HttpRequest, album_key: str, photo_key: str):
    photo = api.check_photo_access(request, album_key, photo_key, "lg")

    previous_filename = photo.key.split("/")[-1]
    next_filename = previous_filename
    back = BackLink("Back to albums", reverse('photo_objects:list_albums'))

    try:
        api.check_album_access(request, photo.album.key)

        album_photos = list(
            photo.album.photo_set.values_list(
                "key", flat=True))
        photo_index = list(album_photos).index(photo.key)
        previous_filename = album_photos[(
            photo_index - 1) % len(album_photos)].split("/")[-1]
        next_filename = album_photos[(
            photo_index + 1) % len(album_photos)].split("/")[-1]

        target = photo.album.title or photo.album.key
        back = BackLink(
            f"Back to {target}", reverse(
                'photo_objects:show_album', kwargs={
                    "album_key": album_key}))
    except AlbumNotFound:
        pass

    details = {
        "Description": render_markdown(photo.description),
        "Timestamp": photo.timestamp,
    }

    return render(request, "photo_objects/photo/show.html", {
        "photo": photo,
        "previous_filename": previous_filename,
        "next_filename": next_filename,
        "title": photo.title or photo.filename,
        "description": photo.description,
        "back": back,
        "details": details,
    })


@json_problem_as_html
def edit_photo(request: HttpRequest, album_key: str, photo_key: str):
    if request.method == "POST":
        try:
            photo = api.modify_photo(request, album_key, photo_key)
            return HttpResponseRedirect(
                reverse(
                    'photo_objects:show_photo',
                    kwargs={
                        "album_key": album_key,
                        "photo_key": photo_key}))
        except FormValidationFailed as e:
            photo = api.check_photo_access(request, album_key, photo_key, "xs")
            form = e.form
    else:
        photo = api.check_photo_access(request, album_key, photo_key, "xs")
        form = ModifyPhotoForm(initial=photo.to_json(), instance=photo)

    target = photo.title or photo.filename
    back = BackLink(
        f'Back to {target}',
        reverse(
            'photo_objects:show_photo',
            kwargs={
                "album_key": album_key,
                "photo_key": photo_key}))

    return render(request, 'photo_objects/form.html', {
        "form": form,
        "title": "Edit photo",
        "back": back,
        "photo": photo,
    })


@json_problem_as_html
def delete_photo(request: HttpRequest, album_key: str, photo_key: str):
    if request.method == "POST":
        api.delete_photo(request, album_key, photo_key)
        return HttpResponseRedirect(
            reverse(
                'photo_objects:show_album',
                kwargs={"album_key": album_key}))
    else:
        photo = api.check_photo_access(request, album_key, photo_key, "xs")
        target = photo.title or photo.filename
        back = BackLink(
            f'Back to {target}',
            reverse(
                'photo_objects:show_photo',
                kwargs={
                    "album_key": album_key,
                    "photo_key": photo_key}))
    return render(request, 'photo_objects/delete.html', {
        "title": "Delete photo",
        "back": back,
        "photo": photo,
        "resource": target,
    })
