# bourbon

Bourbon's a OpenCV-backed API that lets you know whether or not someone is drunk by looking at how they score in a sinusoidal HGN test.

To interface with bourbon, we expose a couple of API endpoints, and those are the following:

`/calibrate`, method=`POST`: This endpoint exists to let the frontend know whether or not the calibration images taken are valid, we accept a payload in the following form:
```json
{
    "min-img-url": "https://urltoimage.com",
    "max-img-url": "https://urltoimage.com"
}
```
Where `min-img-url` is a picture of the person's face with their eyes at the starting position, and `max-img-url` is a picture of their face with their eyes at the ending position.

You'll get back a response of this form, if all is well:
```json
{
    "success": true
}
```

`/tipsy`, method=`POST`: This endpoint exists to give the frontend a sort of "error" letting the frontend know how badly the user does on a HGN test, the lower the better. It takes a payload of the following form:
```json
{
    "min-img-url": "https://urltoimage.com",
    "max-img-url": "https://urltoimage.com",
    "vid-url": "https://urltovid.com"
}
```

You'll get back a response of this form, if all is well:
```json
{
    "success": true,
    "error": 10
}
```
The error could be any number.