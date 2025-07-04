import sys
import base64
import fanbookbotapi
from qcloud_cos import CosConfig, CosS3Client
from rsa import core, PublicKey, transform

def public_key_decrypt(rsa_public_key_pem, qr_code_cipher_b64):
    qr_code_cipher = base64.b64decode(qr_code_cipher_b64)
    public_key = rsa_public_key_pem
    rsa_public_key = PublicKey.load_pkcs1_openssl_pem(public_key)
    cipher_text_bytes = transform.bytes2int(qr_code_cipher)
    decrypted_text = core.decrypt_int(cipher_text_bytes, rsa_public_key.e, rsa_public_key.n)
    final_text = transform.int2bytes(decrypted_text)
    final_qr_code = final_text[final_text.index(0) + 1:]
    return final_qr_code.decode()

rsa_public_key_pem = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDF8yMzDqMl5MpMvfqfo30rnEqF
KtutVKswyURpJD3O94ECE8vC1xtcwYBtCGcppgAvnzjtKJTiZYnLT/KOYlg1yShb
nu0MAtVKASvSbDGgkUGcuBnDsDu2jo40CV9kEcbc5QID5uCXjrr+J1nGoaIMdix8
md+vUFTIZbt+NnxrnQIDAQAB
-----END PUBLIC KEY-----"""




def upload_file_to_cos(secret_id, secret_key, token, upload_path, key_rsa_decrypt=True,file_name=None):
    # 如果需要RSA解密
    if key_rsa_decrypt:
        # RSA解密
        qr_code_cipher_b64 = secret_key
        secret_key = public_key_decrypt(rsa_public_key_pem, qr_code_cipher_b64)
        print("解密后的secret_key:", secret_key)
    region = 'ap-guangzhou'
    bucket = 'fanbook-1251001060'
    host = 'https://fanbook-1251001060.cos.accelerate.myqcloud.com'
    
    # 初始化配置
    config = CosConfig(
        Region=region,
        SecretId=secret_id,
        SecretKey=secret_key,
        Token=token,
        Scheme="https"
    )
    client = CosS3Client(config)

    # 上传本地文件
    local_file_path = file_name # 文件名
    cos_file_path = upload_path + 'v6d85fs41v5dss1v65sda46v45asda.png'# 上传到COS的路径

    try:
        response = client.upload_file(
            Bucket=bucket,
            LocalFilePath=local_file_path,
            Key=cos_file_path,
            PartSize=1,
            MAXThread=10,
            EnableMD5=True
        )
        print("上传成功:", response)
    except Exception as e:
        print("上传失败:", e)

# 参数从https://web.fanbook.cn/api/a1/api/file/cosTmpKey 获取，有效期2小时

if __name__ == "__main__":
    upload_file_to_cos(
        secret_id='AKIDHKppjtC5M5ithMn9C_Kc7Ykv9EStmdkNEkPi7Lm42Q3akkSyCvcoEVBKJumGDArp',
        secret_key='r8HnlXF0F9101W6idDGWJU1JyOETynvh2WN+XDJbCDCSKl9QMIC+pXkTKAjCqgIJkgCOEDfSpGCi5ZJIlpeSZeligMFFKQvTouSv9cV6wmGTWL0ghKg/q9KXYIyWirLeESHh7Cd/CqwO29exVS1J2fOlJWvrE5j49hjKamNlLo4=',
        token='4tsgNEpbeau9Ip8D0A2VBxhqZiHY81Ya684d80e03781f2fc3a8653ffbe60a6483CdQncZoHVv6fjdOK-u9xuGe3wJs1RednTW6KHDN64rEG00gsObG7X5gvEnDpYOeo-dEcnRVmDab_5XfXdc60PWKGElGx5w6ccqW9gsdCSmtV32aZOIhxINhssEWJmYUi7hKu1wGwNyORL_cYTEmwXpAGu7rgMCx7TCLfoIaqn0u1AU3MgcNwTSZU9MPP3mE_OKI1eHJbmIVh_zmFDlxOPUSJa-WR_dxfXTSt-MLa96rfcCwxke0JKw7jW4gQboITda2_HLyWYFXYnTyLlNaUUzghfPsBpj4QRPBJe6rXxIMiQn7FttzYIdo-Kys8gSfcRRdWcMK3frb2XwzzCVN5z-pZnmwqNbxloR56GzI6KrDJ6ok422wEAqUYy33o3lLqmk4tXO7X0-P4j_7_g-CT4yelgXM2ii6YODUnQ6bvvJsi7OAqYaiZetc6kBsK34hH_WynW-oEe69qgZRJaTLC4WYd0ow5rpjXktUkRr4FUDpR7uJjYWRFLtrhByfuhQp8ZYCKy4kEwWxzY_OwOMqGU4RvhHJtc4rlplTPFbh4cj-C21O8215h09fCFKUgDuxNXVP07li6NrCba309Va_wN9493xqo42GhTp6XDqqC1YjUEQhxgme6FKtqHPW4odgamzWj5tTpYZyE2GM50GGwOZqdrAiOUOaIO8WA5cOUL3208uclysrdCRsAaixHh_DjxjMtA4l8eZb6IQAkXm5VV_SZ5-IJPkr8LOctSsz7rM',
        upload_path='/',
        key_rsa_decrypt=True,
        file_name='output.png'
    )