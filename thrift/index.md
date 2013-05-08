---

layout: default

style: |

    #cover {
      background: url('pictures/pipe.png') 75% 85% no-repeat white;
    }

    #thanks {
      background: url('pictures/playfire.png') 87% 42% no-repeat white;
      background-size: 50%;
    }

    #contact {
      background: url('pictures/gmg.png') 87% 38% no-repeat white;
      background-size: 50%;
    }

---

# Python & Scala smoke <br> the peace pipe {#cover}

//Thanks for the image: http://www.schulbilder.org/malvorlage-friedenspfeife-i18756.html


## **how?<br><br>Thrift!**

// The Thrift IDL: **I**nterface **D**efinition **L**anguage. Full stack RPC.


## &nbsp;

- Types
- …Transport
- …Protocol
- …Versioning
- …Processors

// Transparent, high-performance bridge across many programmming languages.




## **types**

// The developer doesn't need to learn another rocket science language for objects serialization or transport.

## Basic

- `bool`
- `byte`
- `i16`, signed.
- `i32`, signed.
- `i64`, signed.
- `double`
- `string`

## Structs

    <mark class="important">struct</mark> TypesExample {
      1: i32 number=10,
      2: i64 bigNumber,
      3: double decimals,
      4: string name="thrifty"
    }

## Containers

- `list <type>` is an ordered list of elements.
- `set <type>` is a unordered set of unique elements.
- `map <type1, type2>` unique keys to values (`dict` in python).

## Exceptions

Like an struct but declared with the exception keyword:

    <mark class="important">exception</mark> IAmNotLearningAnythingException {
      1: string message;
    }

## Services

    <mark class="important">service</mark> amazingScalaMethod {
        string <mark class="important">getHelloWorld</mark>(
            1: string worldName;
        ) throws (
            1: WorldNotFound wnfe;
        )
    }

// As we say in Spain, the **chicha**.




## **transport**

## &nbsp;

- `TFileTransport`, use files.
- …`TFramedTransport`, for non-blocking servers: frames starting with length at the beginning.
- …`TMemoryTransport`, user memory for I/O.
- …`TSocket`, blocking socket.
- …`TZlibTransport`, compressed transport.

// Usually it's used over TCP/IP.

## Is not enough?

If you really need that, you can do that overwritting the `writeMessageBegin()`
for example sending the checksum of your data.




## **protocol**

## &nbsp;

- `TBinaryProtocol`, quicker than text protocols but less debuggable.
- …`TCompactProtocol` & `TDenseProtocol`, compact binary without & with metadata.
- …`TDebugProtocol`, human readable.
- …`TJSONProtocol` & `TSimpleJSONProtocol`, xml? :) SimpleJSON is WO.




## **versioning**

// Needed to read old data from log files or just accept request from
out-of-data clients.

## &nbsp;

Field identifiers (it's better to provide them, if not will be autonumeric
negative number):

    struct Example {
        1: i32 yourLovelyAttrib
        i32 youDoNotLikeThis
    }

// Can also be used on the function arguments.

## Possibilities: adding field

### new server but old client,

the new server will know that the client is outdated & implement default
behaviour for outdated requests.

### new client but old server,

the old server will ignore the extra field.

## Possibilities: removing a field

### new server but old client,

the old client send the field and the new server will ignore it.

### new client but old server <mark>(the most dangerous)</mark>,

no suitable default behaviour. The recommendation is deploy the new server
before the new clients.




## **processors**

## &nbsp;

    interface <mark class="important">TProcessor</mark> {
        bool process(TProtocol in, TProtocol out)
          throws TException
    }

## Similar things out there

- SOAP
- CORBA
- COM
- Pillar
- Protocol buffers




## **demo**

// Just showing a little bit example communicating python and Scala.




## Thanks! {#thanks}

- for listening!
- PyGrunn for bringing me!
- [this FB paper!](http://thrift.apache.org/static/files/thrift-20070401.pdf)




## Contact me {#contact}

- [@agonzalezro](http://twitter.com/agonzalezro)
- [agonzalezro@gmail.com](mailto://agonzalezro@gmail.com)
- [agonzalezro.github.io](http://agonzalezro.github.io)
