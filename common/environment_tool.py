import os

def jiami(input_data:str,pwd:str):
    os.system(
        f'java -cp D:/autoProgram/werun_auto/we_run/test_data\jar\jasypt-1.9.2.jar org.jasypt.intf.cli.JasyptPBEStringEncryptionCLI input="{input_data}" password="{pwd}" algorithm="PBEWithMD5AndDES" keyObtentionIterations=1000  providerName="SunJCE" saltGeneratorClassName="org.jasypt.salt.RandomSaltGenerator" stringOutputType="base64"')

def jiami1(input_data:str,pwd:str):
    os.system(
        f'java -jar D:/autoProgram/werun_auto/we_run/test_data\jar\wz-encryption.jar signKey="{input_data}" password="{pwd}"')


if __name__ == '__main__':
    # 加密
    jiami('A5EEPby3pY&92Nrk', 'A5EEPby3pY&92Nra')
    pass
