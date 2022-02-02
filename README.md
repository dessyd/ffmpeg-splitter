# Splitting Audio With Ffmpeg
From: http://earlh.com/blog/2015/08/08/splitting-audio-with-ffmpeg/

### Local Setup

```bash
# Create virtual environment
python3 -m venv venv
# Activate it
source venv/bin/activate
# make sure pip is up to date
pip install --upgrade pip
# install project's requirements
pip install -r requirements.txt 
```
### To Do 

- [ ] Put config outside of code
- [x] Add subsecond timing
- [x] Force "overwrite tracks"
- [ ] Set "overwrite tracks" as parameter
- [ ] Remove video track (ffmpeg )
- [ ] Check qscale parameter
- [ ] Add Illustration
- [ ] Add Album 1 of 1 tag