# Qué es una cartera de Bitcoin

Para poder comprender lo que es una cartera, o wallet, de Bitcoin se tienen que tener claro los conceptos de llave privada (k), llave pública (K) y la dirección (A). La k en minúsculas hace referencia a la llave privada, y en mayúsculas hace referencia a la manera con la que se puede compartir.

## Llave privada

La llave privada es un número aleatorio astronómicamente grande. Se trata de un número entero entre `0` y casi `2^256`. Quiero enfatizar el casi, porque se trata de una de las propiedades matemáticas importantes de Bitcoin.

El límite superior real se trata del número primo más cercano y menor a `2^256`. En Python se puede calcular fácilmente.

```python
p = 2**256 - 2**32 - 977
```

El hecho de que se utilice este número primo particular es porque para que las matemáticas del algoritmo criptográfico funcione, se requiere un número primo.

El algoritmo de curva elíptica ECDSA, **Elliptic Curve Digital Signature Algorithm**, además de utilizar la constante y número primo, `p`, toma otros parámetros definidos por la curva `secp256k1`. Dicha curva es el estándar de Bitcoin, otro de los parámetros que define es el que se conoce como generador (G).

Un generador es una constante que representa una coordenada (x, y) dentro del plano criptográfico. Los parámetros de la curva `secp256k1` se muestran a continuación.

```python
# Número primo
p = 2**256 - 2**32 - 977

# Generador en xy
Gx = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
Gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8

# Orden del grupo
N = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
```

Notar que los números que comienzan con `0x`, en Python, son números hexadecimal.

Los parámetros nos permiten construír de manera determinística una llave pública a partir del número aleatorio, o llave privada, aplicando una operación criptográfica, que se puede representar como una multiplicación.

```python
K = k * G
```

La operación no es una multiplicación tal cual la conocemos, se trata de una operación criptográfica, que nos permite plantear la siguiente analogía.

Tenemos nuestro número secreto y un generador. La multiplicación resulta en otra coordenada xy para K, o la llave pública. Por lo tanto, la persona que tenga k, puede sin problemas generar K, reclamando los Bitcoins, si es que hay alguno, en dicha llave pública.

La operación criptográfica lo que permite es que esta operación no pueda ser revertida. Lo que quiere decir que de la ecuación anterior no se puede despejar para k. No es posible dividir mi llave pública entre el generador para obtener k. Esto se conoce como asimétria, porque la ecuación solo puede resolverse de un lado, y no hacia el otro.

```
         -- multiplicación criptográfica -->
privada                                       pública
         <--- operación irreversible -------
```

La acción de revertir la multiplicación criptográfica se conoce como `el problema de log discreto`.

Después de la analogía, lo más importante de recalcar es que la llave privada está protegida utilizando el algoritmo de ECSDA. Mucho se estipula de que en un futuro próximo, el algoritmo pueda ser descifrado por una computadora cuántica. 

Si este hipotético caso se diera, aún así los bitcoins que guardamos comúnmente en una cartera, se encuentran referenciando una dirección, lo que añade 2 capas más de protección por encima de la llave pública. 

como ya mencionamos una llave pública es una coordenada xy, lo que se necesita es hacer una operación conocida como serialización, para convertir un punto xy en un solo valor. 




entropia y nmenomicas


El algoritmo que utiliza Bitcoin se 


El algori

para que se pueda utilizar el algoritmo de curva elíptica, ECDSA


De hecho, si consideramos que el número de átomos


Existe una relación criptográfica entre ellas.


Esta se trata de la primera entrega de una serie de 7 textos sobre Bitcoin. 


    ECDSA
    qué es una paper wallet.

