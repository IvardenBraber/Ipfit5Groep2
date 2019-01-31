"""
-------------------------------------------------------------------------------
Copyright 2015 Destruct_Icon
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
-------------------------------------------------------------------------------
http://www.malwerewolf.com/
Author: Destruct_Icon, nanoSpl0it
Version: 1.0
Summary: Queries Virus Total for all reports of the hashes provided.
"""
import requests
import argparse
import os
import time
import requests
import urllib3

malware_respons = []
malware_naam = []
malware_return = []
malware_file = []
api_key = "ea44595e28b22f726e1fe8891943439afe787a180da42cf736f4200274b67931"


def VT_Request(key, hash, name):
    params = {'apikey': key, 'resource': hash}
    url = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params)
    json_response = url.json()
    # print(json_response)
    file_malicous = False
    response = int(json_response.get('response_code'))
    if response == 0:
        file_malicous = False

    elif response == 1:
        positives = int(json_response.get('positives'))
        if positives == 0:
            file_malicous = False

        else:
            file_malicous = True
            malware_return.append(hash)
            malware_naam.append(name)

    else:
        print(hash + ' could not be searched. Please try again later.')


class virustotal_script():

    def checkkey(kee):
        try:
            if len(kee) == 64:
                return kee
            else:
                print("There is something wrong with your key. Not 64 Alpha Numeric characters.")
                exit()
        except e:
            print(e)


    def checkhash(hsh):
        try:
            if len(hsh) == 32:
                return hsh
            elif len(hsh) == 40:
                return hsh
            elif len(hsh) == 64:
                return hsh
            else:
                print("The Hash input does not appear valid.")
                exit()
        except:
            print("foutje")


    def fileexists(filepath):
        try:
            if os.path.isfile(filepath):
                return filepath
            else:
                print("There is no file at:" + filepath)
                exit()
        except e:
            print(e)


    def program_start():
        parser = argparse.ArgumentParser(description="Query hashes against Virus Total.")
        parser.add_argument('-i', '--input', type=fileexists, required=False,
                            help='Input File Location EX: /Desktop/Somewhere/input.txt')
        parser.add_argument('-o', '--output', required=True, help='Output File Location EX: /Desktop/Somewhere/output.txt ')
        parser.add_argument('-H', '--hash', type=checkhash, required=False,
                            help='Single Hash EX: d41d8cd98f00b204e9800998ecf8427e')
        parser.add_argument('-k', '--key', type=checkkey, required=True, help='VT API Key EX: ASDFADSFDSFASDFADSFDSFADSF')
        parser.add_argument('-u', '--unlimited', action='store_const', const=1, required=False,
                            help='Changes the 26 second sleep timer to 1.')
        args = parser.parse_args()






    def main(data_dic: dict, name):
        multiple_files = True

        # Run for a single hash + key
        if multiple_files == False:
            VT_Request(api_key, hash, name)
        # Run for an input file + key
        else:
            for key in data_dic:
                VT_Request(api_key, key, data_dic.get(key))

        return malware_naam

