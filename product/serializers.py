
from rest_framework.serializers import ModelSerializer
from product.models import Product
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes



class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'marja', 'package_code')

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        price = representation.get('price')
        marja = representation.get('marja')
        package_code = representation.get('package_code')

        price_bytes = str(price).encode('utf-8') if price is not None else b''
        marja_bytes = str(marja).encode('utf-8') if marja is not None else b''
        package_code_bytes = str(package_code).encode('utf-8') if package_code is not None else b''

        key = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_CFB)

        cipher_text_price = cipher.encrypt(price_bytes)
        cipher_text_marja = cipher.encrypt(marja_bytes)
        cipher_text_package_code = cipher.encrypt(package_code_bytes)

        iv = cipher.iv
        representation.pop('price')
        representation.pop('marja')
        representation.pop('package_code')

        representation['encrypted_price'] = cipher_text_price.hex()
        representation['encrypted_marja'] = cipher_text_marja.hex()
        representation['encrypted_package_code'] = cipher_text_package_code.hex()

        return representation

