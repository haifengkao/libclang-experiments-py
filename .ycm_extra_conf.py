#!/usr/local/bin/python

flags = ['-x', 'objective-c',
        '-arch', 'arm64',
        '-fmodules',
        '-miphoneos-version-min=9.3',
        '-isysroot', '/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS.sdk'
        ]

def FlagsForFile( filename, **kwargs ):
  return {
    'flags': flags,
    'do_cache': True
  }
