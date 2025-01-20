# GLaDOS Voice Pack for Dreame Vacuum Robots

Uses voice generation by [15.ai](https://15.ai/).

MD5 sum of the prepackaged `voice_pack.tar.gz`:  
`8ebfabb9e23e169a5c9b867266f9d1ef`

Works at least with `L10 Pro`, `Z10 Pro`, `W10`, `D9` and `F9`

## Installation

1. In Valetudo go to "Robot Settings" -> "Misc Settings"
1. Enter the following information in the "Voice packs" section:
    - URL: `https://github.com/Findus23/voice_pack_dreame/raw/main/voice_pack.tar.gz`
    - Language Code: `GLA`
    - Hash: `8ebfabb9e23e169a5c9b867266f9d1ef`
    - File size: `4325024` byte
1. Click "Set Voice Pack"

Interestingly on my L10 Pro running `Valetudo 2022.03.0` the .tar.gz doesn't seem to work and the newly created folder `/data/personalized_voice/GLA` stays empty.
However, the language code is set correctly in Valetudo and manually copying the files into the right directory works:

```
git clone https://github.com/Findus23/voice_pack_dreame
scp voice_pack_dreame/output/* root@<YOUR_ROBOT_ADDRESS>:/data/personalized_voice/GLA
```

-----
Thanks to https://github.com/ccoors/dreame_voice_packs for the inspiration and the list of sounds and 15.ai for the voice generation.
