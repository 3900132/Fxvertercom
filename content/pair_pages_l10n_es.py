# -*- coding: utf-8 -*-
"""Contenidos en español para las páginas de pares de divisas ("USD a EUR").

PAIR_UI_L10N corresponde a las cadenas de pair_pages.PAIR_UI["en"] (los
marcadores {f} {t} {d} se mantienen intactos). PAIR_CONTENT_L10N corresponde
a los 15 pares de PAIR_CONTENT["en"], con claves idénticas a la versión
inglesa. build-lang-pages.py fusiona ambos en PAIR_UI / PAIR_CONTENT.
"""

PAIR_UI_L10N = {
    "pairConvert": "Conversor en vivo",
    "pairRateHead": "Tipo de cambio actual",
    "pairAsOf": "Tipo de referencia del {d}. El conversor en vivo de arriba consulta siempre el tipo más reciente — las tablas de abajo son una instantánea del momento de generación, solo como orientación.",
    "pairAmounts": "Importes habituales: {f} a {t}",
    "pairReverse": "Importes habituales: {t} a {f}",
    "pairMore": "Más conversiones de {f}",
    "pairMorePairs": "Más pares de divisas",
    "pairIntroHead": "Sobre el tipo de cambio {f} a {t}",
    "pairCurLinks": "Páginas de divisas",
    "pairMetaTmpl": ("Convierte {f} a {t} con tipos de cambio en vivo: el tipo {f}/{t} de hoy, una calculadora gratuita, "
                     "tablas de importes habituales y qué mueve este par de divisas."),
}

PAIR_CONTENT_L10N = {
    # ───────────────────────── USD → EUR ─────────────────────────
    "USD-EUR": {
        "title": "USD a EUR — Tipo de cambio, conversor y tablas",
        "description": "Convierte dólares estadounidenses a euros con tipos en vivo: el tipo de cambio USD/EUR de hoy, una calculadora gratuita, tablas de importes y qué mueve el par.",
        "h1": "USD a EUR — convertir dólares estadounidenses a euros",
        "intro": [
            "USD/EUR es el par de divisas más operado del mundo — cerca de un cuarto de todo el volumen de divisa —, y por eso tiene los diferenciales más estrechos y el mercado más profundo de cualquier conversión. El tipo es, sencillamente, el precio de un dólar estadounidense en euros, fijado de forma continua por el comercio global, los flujos de inversión y la brecha de tipos de interés entre la Reserva Federal y el Banco Central Europeo.",
            "Para las conversiones cotidianas, la pregunta práctica es cuánto margen pagas sobre el tipo medio del mercado que se muestra aquí. Los bancos suelen añadir entre un 1 % y un 4 %; las tarjetas y los servicios de transferencia varían mucho. Consultar el tipo en vivo antes de una compra o una transferencia te dice al instante si una oferta es justa.",
        ],
        "faq": [
            ("¿Cómo se determina el tipo de cambio de USD a EUR?",
             "Flota libremente — la oferta y la demanda de las dos monedas fijan el precio las 24 horas, influidas sobre todo por la política de tipos de la Fed y el BCE, la inflación a ambos lados del Atlántico y el sentimiento global de riesgo. No existe un objetivo fijo ni gestionado."),
            ("¿Cuándo es el mejor momento para convertir USD a EUR?",
             "La liquidez es más profunda y los diferenciales más estrechos durante el solape de las horas de negociación europea y estadounidense (aproximadamente de 13:00 a 17:00 UTC). Nadie puede predecir con fiabilidad la dirección a corto plazo, así que con importes grandes es más seguro convertir en partes que esperar un día mejor."),
        ],
    },
    # ───────────────────────── USD → GBP ─────────────────────────
    "USD-GBP": {
        "title": "USD a GBP — Tipo de cambio, conversor y tablas",
        "description": "Convierte dólares estadounidenses a libras esterlinas con tipos en vivo: el tipo de cambio USD/GBP de hoy, una calculadora gratuita y tablas de importes habituales.",
        "h1": "USD a GBP — convertir dólares estadounidenses a libras esterlinas",
        "intro": [
            "El tipo entre el dólar y la libra, apodado «cable» por el cable telegráfico transatlántico que lo transmitió por primera vez en la década de 1860, es una de las cotizaciones de cambio más antiguas del mundo que se siguen publicando sin interrupción. Hoy refleja la brecha de tipos entre la Reserva Federal y el Banco de Inglaterra, la inflación británica y la salud del comercio y las finanzas públicas del Reino Unido.",
            "La libra se negocia con más actividad durante las horas de Londres, y el par tiende a dar giros bruscos en torno a los datos económicos y los anuncios fiscales británicos. Comparar cualquier oferta con el tipo medio del mercado de abajo es la forma más rápida de ver cuánto margen se queda un proveedor.",
        ],
        "faq": [
            ("¿Por qué la libra esterlina vale más que el dólar estadounidense?",
             "Un precio unitario más alto no significa una economía más fuerte — refleja la historia y las denominaciones. La libra fue la moneda dominante del mundo cuando el dólar aún no existía; la cifra en sí no dice nada sobre la fuerza económica relativa ni el poder adquisitivo."),
            ("¿Qué mueve más al USD/GBP?",
             "Las decisiones de tipos de la Fed y el Banco de Inglaterra, los datos de inflación británicos y las noticias políticas o fiscales de Westminster. En el voto del Brexit de 2016 la libra cayó cerca de un 10 % en un día — un recordatorio de que la esterlina carga con un riesgo político que la mayoría de las grandes monedas no conoce."),
        ],
    },
    # ───────────────────────── USD → JPY ─────────────────────────
    "USD-JPY": {
        "title": "USD a JPY — Tipo de cambio, conversor y tablas",
        "description": "Convierte dólares estadounidenses a yenes japoneses con tipos en vivo: el tipo de cambio USD/JPY de hoy, una calculadora gratuita y qué mueve al yen.",
        "h1": "USD a JPY — convertir dólares estadounidenses a yenes japoneses",
        "intro": [
            "USD/JPY es el segundo par de divisas más operado del mundo y el barómetro clásico de la brecha de tipos de interés entre Estados Unidos y Japón. Como los tipos japoneses rondaron cero durante décadas, el yen se convirtió en la moneda de financiación favorita del mundo — se debilita cuando los mercados están confiados y se fortalece con fuerza cuando las crisis deshacen esas posiciones.",
            "Al par también se le sigue la pista por las intervenciones oficiales japonesas: el Ministerio de Finanzas ha comprado yenes repetidamente cuando se debilita demasiado y demasiado rápido. Las conversiones grandes conviene cotejarlas con el tipo medio del mercado, porque los márgenes minoristas del JPY pueden ser engañosamente anchos.",
        ],
        "faq": [
            ("¿Por qué el yen a veces cae tanto frente al dólar?",
             "Sobre todo por la brecha de tipos de interés. Cuando los tipos estadounidenses son altos y los japoneses siguen cerca de cero, los inversores venden yenes para comprar activos en dólares de mayor rentabilidad — el carry trade. El yen puede deslizarse durante meses y luego saltar con violencia cuando esas posiciones se deshacen."),
            ("¿Puede el gobierno japonés cambiar el tipo USD/JPY?",
             "Puede ir contra el mercado, no invertirlo. Japón ha intervenido comprando o vendiendo yenes cuando los movimientos se volvían desordenados, a veces con decenas de miles de millones de dólares en un solo episodio. La intervención suaviza el camino; rara vez cambia la dirección de largo plazo que marcan los fundamentos."),
        ],
    },
    # ───────────────────────── USD → CNY ─────────────────────────
    "USD-CNY": {
        "title": "USD a CNY — Tipo de cambio, conversor y tablas",
        "description": "Convierte dólares estadounidenses a yuanes chinos con tipos en vivo: el tipo de cambio USD/CNY de hoy, una calculadora gratuita y cómo funciona el tipo gestionado.",
        "h1": "USD a CNY — convertir dólares estadounidenses a yuanes chinos",
        "intro": [
            "El tipo entre el dólar y el yuan es el mayor par de divisas gestionado por un banco central. Cada mañana el Banco Popular de China fija un tipo central diario, y el tipo onshore (CNY) solo puede moverse dentro de una banda alrededor de él — por eso USD/CNY se mueve mucho menos de un día para otro de lo que sugiere su importancia económica.",
            "El superávit comercial de China, los controles de capital y los objetivos de política moldean el tipo. Para las conversiones, ten en cuenta que el CNY onshore y el CNH offshore pueden diferir ligeramente, y que la conversión de divisa de particulares en China está sujeta a reglas de control de capital. Compara siempre las ofertas con el tipo de referencia de abajo.",
        ],
        "faq": [
            ("¿Es convertible libremente el yuan chino?",
             "No del todo. La conversión ligada al comercio es fácil, pero los flujos de inversión a través de la frontera están controlados por cupos y aprobaciones. Por eso la versión offshore (CNH) cotiza a un precio ligeramente distinto del CNY onshore — la brecha refleja lo caro que resulta mover dinero a través de la frontera."),
            ("¿Por qué USD/CNY apenas se mueve comparado con otros pares?",
             "Porque lo gestiona el banco central. El tipo central diario y la banda de negociación mantienen el tipo estable frente al dólar, en línea con la preferencia de China por la previsibilidad en el comercio. Gestionado no significa fijo: con los meses y los años, el tipo sigue la tendencia de los fundamentos."),
        ],
    },
    # ───────────────────────── USD → INR ─────────────────────────
    "USD-INR": {
        "title": "USD a INR — Tipo de cambio, conversor y tablas",
        "description": "Convierte dólares estadounidenses a rupias indias con tipos en vivo: el tipo de cambio USD/INR de hoy, una calculadora gratuita y qué mueve a la rupia.",
        "h1": "USD a INR — convertir dólares estadounidenses a rupias indias",
        "intro": [
            "USD/INR es uno de los corredores de remesas más importantes del mundo — India recibe más remesas que ningún otro país — y un par emergente muy operado. El Banco de la Reserva de India gestiona la volatilidad, no el nivel: suaviza los movimientos bruscos con sus reservas pero deja que la rupia encuentre su tendencia de largo plazo.",
            "La historia secular de la rupia es una depreciación gradual frente al dólar, impulsada por los diferenciales de inflación y la balanza por cuenta corriente de India, salpicada por los episodios globales de riesgo. Para quien envía dinero a India, la brecha entre el tipo medio del mercado y el tipo ofrecido es donde se esconde el coste real.",
        ],
        "faq": [
            ("¿Por qué la rupia india se deprecia con el tiempo?",
             "Sobre todo por los diferenciales de inflación y el déficit comercial: India importa mucho más de lo que exporta, y la diferencia se financia con entradas de capital. El RBI suaviza el camino, pero durante décadas la rupia se ha debilitado de forma constante frente al dólar — algo normal en una economía en desarrollo."),
            ("¿Cómo consigo el mejor tipo al enviar dinero a India?",
             "Compara el tipo ofrecido con el tipo medio del mercado antes de enviar, y no solo las comisiones. Los servicios especializados en remesas suelen batir a las transferencias bancarias en este corredor, y una diferencia de incluso el 1 % es significativa en transferencias familiares regulares a lo largo de un año."),
        ],
    },
    # ───────────────────────── USD → CAD ─────────────────────────
    "USD-CAD": {
        "title": "USD a CAD — Tipo de cambio, conversor y tablas",
        "description": "Convierte dólares estadounidenses a dólares canadienses con tipos en vivo: el tipo de cambio USD/CAD de hoy, una calculadora gratuita y qué mueve al loonie.",
        "h1": "USD a CAD — convertir dólares estadounidenses a dólares canadienses",
        "intro": [
            "USD/CAD — el «loonie» — es un par de divisas del top cinco mundial construido sobre una de las mayores relaciones comerciales del planeta. Canadá envía en torno a tres cuartas partes de sus exportaciones a Estados Unidos, así que el par se negocia al compás del crecimiento estadounidense, de los precios de la energía (Canadá es un gran exportador de petróleo) y de la brecha de tipos entre la Fed y el Banco de Canadá.",
            "Cuando el petróleo sube, el CAD típicamente se fortalece; cuando golpean los temores al crecimiento global, se debilita junto con las monedas de materias primas en general. El par es líquido a toda hora, y encontrar ofertas a una fracción de punto del tipo medio del mercado es fácil — así que los márgenes anchos siempre merecen cuestionarse.",
        ],
        "faq": [
            ("¿Por qué al dólar canadiense lo llaman loonie?",
             "Por el somormujo (loon) grabado en la moneda de un dólar introducida en 1987. El apodo prendió y hoy nombra a la propia moneda en la jerga de divisas, como en «el loonie se revalorizó hoy»."),
            ("¿De verdad afecta el precio del petróleo al USD/CAD?",
             "Sí, de forma visible. El crudo y sus derivados son la mayor categoría exportadora de Canadá, de modo que un petróleo al alza suele traer más dólares a Canadá y elevar al CAD. Los operadores tratan el par como una apuesta aproximada a los mercados energéticos, además de a los tipos de interés de los dos países."),
        ],
    },
    # ───────────────────────── USD → AUD ─────────────────────────
    "USD-AUD": {
        "title": "USD a AUD — Tipo de cambio, conversor y tablas",
        "description": "Convierte dólares estadounidenses a dólares australianos con tipos en vivo: el tipo de cambio USD/AUD de hoy, una calculadora gratuita y qué mueve al aussie.",
        "h1": "USD a AUD — convertir dólares estadounidenses a dólares australianos",
        "intro": [
            "El dólar australiano es la moneda de materias primas por excelencia: su suerte sigue al mineral de hierro, al carbón y al gas, y sobre todo a la demanda china de los tres. USD/AUD es por eso uno de los indicadores en tiempo real más limpios del apetito global por el riesgo — el aussie se fortalece cuando el comercio mundial bulle y se debilita en los episodios de huida del riesgo.",
            "La política de tipos del Banco de la Reserva de Australia y de la Fed gobierna los vaivenes a corto plazo. Las poblaciones de estudiantes y de visas working holiday hacen de USD→AUD (y de vuelta) una conversión recurrente habitual, donde incluso un margen del 1 % se acumula con rapidez.",
        ],
        "faq": [
            ("¿Por qué el dólar australiano es tan sensible a China?",
             "China es, con mucha diferencia, el mayor mercado exportador de Australia, sobre todo de mineral de hierro para la siderurgia. Cuando la construcción china se frena, los precios de las materias primas y el AUD suelen caer juntos — la moneda funciona como un barómetro en tiempo real de la industria pesada china."),
            ("¿Es el AUD un valor refugio?",
             "Justo lo contrario: los operadores lo llaman una moneda de riesgo. En los pánicos globales — 2008, 2020 — el dinero fluye hacia el dólar estadounidense y el aussie tiende a caer más que ninguna otra moneda importante. Esa naturaleza cíclica es justamente la razón por la que los operadores de carry y los observadores del crecimiento lo vigilan tan de cerca."),
        ],
    },
    # ───────────────────────── USD → CHF ─────────────────────────
    "USD-CHF": {
        "title": "USD a CHF — Tipo de cambio, conversor y tablas",
        "description": "Convierte dólares estadounidenses a francos suizos con tipos en vivo: el tipo de cambio USD/CHF de hoy, una calculadora gratuita y qué mueve al franco.",
        "h1": "USD a CHF — convertir dólares estadounidenses a francos suizos",
        "intro": [
            "El franco suizo es la moneda refugio por antonomasia: cuando estalla una guerra, una tensión bancaria o un pánico de mercado, el dinero fluye hacia Suiza y el CHF se fortalece. USD/CHF tiende por eso a caer en las crisis globales incluso cuando el propio dólar es un refugio — el franco es simplemente el refugio más fuerte.",
            "El Banco Nacional Suizo moldea el tipo de forma activa, desde el famoso suelo frente al euro de 2011–2015 hasta la intervención intensiva posterior. Para las conversiones, Suiza es también un recordatorio de que un par de un país rico puede seguir cargando márgenes minoristas anchos, sobre todo en aeropuertos y hoteles — consulta siempre la referencia del tipo medio del mercado.",
        ],
        "faq": [
            ("¿Por qué se considera el franco suizo un valor refugio?",
             "Un siglo de neutralidad, poca deuda, un superávit por cuenta corriente y un banco central creíble hacen del franco el aparcamiento por defecto del dinero que huye del riesgo. La inflación suiza, además, ha corrido durante décadas muy por debajo de la de EE. UU. y la eurozona, preservando el poder adquisitivo de la moneda."),
            ("¿Qué hizo el BNS en enero de 2015?",
             "Abandonó de golpe su límite a la fortaleza del franco frente al euro. USD/CHF y EUR/CHF se desplomaron entre un 20 % y un 30 % en cuestión de minutos — uno de los mayores movimientos intradía jamás vistos en un par principal, y la razón por la que los operadores aún respetan la expresión «riesgo BNS»."),
        ],
    },
    # ───────────────────────── USD → MXN ─────────────────────────
    "USD-MXN": {
        "title": "USD a MXN — Tipo de cambio, conversor y tablas",
        "description": "Convierte dólares estadounidenses a pesos mexicanos con tipos en vivo: el tipo de cambio USD/MXN de hoy, una calculadora gratuita y qué mueve al peso.",
        "h1": "USD a MXN — convertir dólares estadounidenses a pesos mexicanos",
        "intro": [
            "USD/MXN es el par emergente más operado de América y uno de los más líquidos del mundo. El peso se negocia con todo lo que mueve a la economía estadounidense — política comercial, crecimiento, brechas de tipos entre la Fed y Banxico —, más los precios del petróleo y el enorme corredor de remesas desde Estados Unidos.",
            "Por lo líquido que es, el par reacciona con velocidad al sentimiento global de riesgo: es un objetivo clásico del carry trade que se fortalece en los mercados tranquilos y da saltos violentos en los pánicos. Para viajeros y remitentes, márgenes del 3 % al 6 % son habituales en los aeropuertos — el tipo medio del mercado de abajo es la referencia con la que comparar.",
        ],
        "faq": [
            ("¿Por qué USD/MXN es tan volátil?",
             "Los tipos de interés altos de México atraen dinero especulativo a corto plazo que se va con la misma rapidez en las tensiones; el peso es además el activo de referencia de todo el comercio y las noticias políticas entre EE. UU. y México. La combinación lo hace líquido pero nervioso — los movimientos diarios grandes son lo normal, no un fallo."),
            ("¿Cuál es la forma más barata de enviar dólares a México?",
             "Los servicios especializados en remesas baten de forma consistente a bancos y locales de envío de efectivo en este corredor. Compara el importe entregado con el tipo medio del mercado: en una transferencia de 300 dólares, la diferencia entre una oferta justa y un margen del 5 % puede equivaler al salario local de un día entero."),
        ],
    },
    # ───────────────────────── USD → PHP ─────────────────────────
    "USD-PHP": {
        "title": "USD a PHP — Tipo de cambio, conversor y tablas",
        "description": "Convierte dólares estadounidenses a pesos filipinos con tipos en vivo: el tipo de cambio USD/PHP de hoy, una calculadora gratuita y qué mueve al peso.",
        "h1": "USD a PHP — convertir dólares estadounidenses a pesos filipinos",
        "intro": [
            "El peso filipino se ancla en uno de los mayores flujos de remesas del mundo: millones de trabajadores filipinos en el extranjero envían dinero a casa, y esas entradas de dólares son un pilar de la economía. USD/PHP se negocia, en consecuencia, según el apetito global por el riesgo, los precios del petróleo (Filipinas es importador neto) y la política del Bangko Sentral ng Pilipinas.",
            "El tipo oficial se gestiona con mano ligera — el banco central permite el ajuste gradual mientras suaviza los picos. Para las familias de los trabajadores emigrados y los viajeros, la dispersión entre proveedores en este corredor es amplia, así que mirar el tipo medio del mercado antes de enviar es la forma más sencilla de ahorrar.",
        ],
        "faq": [
            ("¿Cómo afectan las remesas al peso filipino?",
             "Las entradas constantes de dólares de los trabajadores en el exterior sostienen al peso y a la balanza de pagos del país — varios puntos del PIB cada año. Cuando sube el riesgo global o flaquean las economías de destino, las remesas se moderan y el peso tiende a seguirlas."),
            ("¿Conviene más convertir USD a PHP en Estados Unidos o en Filipinas?",
             "Depende del proveedor, no del país. En ambos lados del corredor hay opciones baratas y caras; la cifra decisiva es cuántos pesos recibe realmente el destinatario. Compara ofertas contra el tipo medio del mercado en lugar de fiarte del local más cercano."),
        ],
    },
    # ───────────────────────── EUR → GBP ────────────────────────
    "EUR-GBP": {
        "title": "EUR a GBP — Tipo de cambio, conversor y tablas",
        "description": "Convierte euros a libras esterlinas con tipos en vivo: el tipo de cambio EUR/GBP de hoy, una calculadora gratuita, tablas de importes y qué mueve este par.",
        "h1": "EUR a GBP — convertir euros a libras esterlinas",
        "intro": [
            "EUR/GBP es el cruce europeo clásico: dos economías que se envían en torno a la mitad de su comercio, separadas por una sola frontera de divisa. Como ambas son monedas desarrolladas y de baja inflación, el par se mueve mucho menos que los cruces con el dólar — en el fondo es una apuesta a las fortunas relativas de la eurozona y el Reino Unido.",
            "La brecha de tipos entre el BCE y el Banco de Inglaterra gobierna la mayor parte de la tendencia, mientras que las noticias políticas y fiscales británicas provocan los picos. Para trabajadores transfronterizos, pensionistas y empresas, la estabilidad del par hace que las diferencias pequeñas de tipo importen aún más: un margen del 1 % es una buena parte del movimiento anual total.",
        ],
        "faq": [
            ("¿Por qué EUR/GBP es más tranquilo que EUR/USD?",
             "Ni el euro ni la libra son monedas globales de riesgo, así que las grandes huidas hacia la seguridad las pasan de largo. El par refleja sobre todo la economía relativa Reino Unido–UE y los diferenciales de tipos, que cambian despacio — aunque puede dispararse con las noticias políticas británicas, como mostró 2016."),
            ("¿Cómo sigue afectando el Brexit al EUR/GBP?",
             "Estructuralmente. Las nuevas fricciones comerciales desde 2021 hicieron la economía británica algo menos abierta a la UE, lo que la mayoría de los economistas vincula a una esterlina estructuralmente más débil. Cada ronda de negociaciones Reino Unido–UE sobre reglas comerciales sigue moviendo el par."),
        ],
    },
    # ───────────────────────── EUR → CHF ────────────────────────
    "EUR-CHF": {
        "title": "EUR a CHF — Tipo de cambio, conversor y tablas",
        "description": "Convierte euros a francos suizos con tipos en vivo: el tipo de cambio EUR/CHF de hoy, una calculadora gratuita y el papel del Banco Nacional Suizo en el par.",
        "h1": "EUR a CHF — convertir euros a francos suizos",
        "intro": [
            "EUR/CHF es el test de fuego refugio de Europa: cada vez que sube la tensión en la eurozona — la crisis de deuda de 2011, los sustos bancarios, la guerra en el continente — el dinero cruza la frontera suiza y el par cae. El Banco Nacional Suizo lo vigila más que a ningún otro tipo y ha intervenido repetidamente para evitar que el franco asfixie las exportaciones suizas.",
            "La historia moderna del par es dramática: un suelo en 1,20 desde 2011 y luego el desanclaje de enero de 2015, que produjo un flash crash del 20–30 % en minutos. Desde entonces el franco se negocia como un refugio limpio, aunque a veces demasiado fuerte — y el BNS sigue siendo un participante activo en este mercado.",
        ],
        "faq": [
            ("¿Por qué le importa tanto el EUR/CHF al Banco Nacional Suizo?",
             "Porque la economía suiza vende a Europa. Un franco demasiado fuerte hace poco competitivas las exportaciones suizas y arrastra la inflación por debajo del objetivo, así que el BNS compra divisa extranjera (y en su día impuso tipos negativos) para limitar la fortaleza del franco. Interviene en este par más que casi cualquier otro banco central en un mercado importante."),
            ("¿Es EUR/CHF un par estable para mantener?",
             "Es estable en tiempos tranquilos y explosivo en las crisis — justo lo contrario de diversificado. El desanclaje de 2015 sigue siendo la advertencia de manual de que la promesa de un banco central de limitar una moneda puede retirarse de la noche a la mañana. Quien trató el par como exento de riesgo aprendió lo contrario en una sola mañana."),
        ],
    },
    # ───────────────────────── EUR → PLN ────────────────────────
    "EUR-PLN": {
        "title": "EUR a PLN — Tipo de cambio, conversor y tablas",
        "description": "Convierte euros a eslotis polacos con tipos en vivo: el tipo de cambio EUR/PLN de hoy, una calculadora gratuita y qué mueve al esloti.",
        "h1": "EUR a PLN — convertir euros a eslotis polacos",
        "intro": [
            "Polonia es la sexta economía de la Unión Europea que aún usa moneda propia, y el esloti es la más operada de las monedas de la UE fuera del euro. EUR/PLN se negocia según la brecha de tipos con el Banco Nacional de Polonia, los fondos de la UE que fluyen hacia el este, los pedidos de la industria alemana a la polaca y el riesgo geopolítico regional.",
            "Desde que Polonia entró en la UE en 2004, el esloti se ha fortalecido en los auges y ha caído con fuerza en las crisis — 2008 y 2022 llevaron el par a extremos históricos. Con la eventual adopción del euro aún sin decidir, el par seguirá siendo una pieza estructural de las finanzas europeas durante años.",
        ],
        "faq": [
            ("¿Adoptará Polonia el euro y eliminará el esloti?",
             "Polonia está obligada legalmente a entrar en el euro tarde o temprano, pero no tiene fecha objetivo y el escepticismo público es amplio. Mientras no exista un calendario creíble de adopción, EUR/PLN seguirá siendo un par muy operado — las declaraciones políticas sobre el calendario pueden moverlo por sí solas."),
            ("¿Por qué se disparó EUR/PLN en 2022?",
             "La guerra en la vecina Ucrania convirtió a Polonia en economía de primera línea de un día para otro: entradas de refugiados, gasto en defensa y choques energéticos golpearon con dureza a la moneda. El Banco Nacional de Polonia intervino para sostener al esloti — los movimientos más bruscos del par en dos décadas."),
        ],
    },
    # ───────────────────────── GBP → JPY ────────────────────────
    "GBP-JPY": {
        "title": "GBP a JPY — Tipo de cambio, conversor y tablas",
        "description": "Convierte libras esterlinas a yenes japoneses con tipos en vivo: el tipo de cambio GBP/JPY de hoy, una calculadora gratuita y qué mueve a este par volátil.",
        "h1": "GBP a JPY — convertir libras esterlinas a yenes japoneses",
        "intro": [
            "GBP/JPY — los veteranos lo llamaban «la bestia» o «el dragón» — es uno de los pares principales más volátiles. Apila dos motores de riesgo: la sensibilidad de la esterlina a las noticias políticas y fiscales británicas, y el papel del yen como moneda de financiación mundial, que lo hace oscilar con fuerza cada vez que el sentimiento global gira.",
            "El par es el favorito del carry trade: pedir prestados yenes a tipos casi nulos para comprar libras de mayor rendimiento. Funciona hasta que una crisis obliga a todos a deshacer posiciones a la vez, y por eso GBP/JPY tiende a subir a fuego lento durante años y a caer con violencia en semanas. Aquí el tamaño y el momento importan más que en casi cualquier otro par principal.",
        ],
        "faq": [
            ("¿Por qué GBP/JPY es más volátil que USD/JPY?",
             "Porque multiplica dos volatilidades. La esterlina añade el riesgo político y económico británico por encima del sentimiento global que ya mueve al USD/JPY. El par no comparte economía ancla alguna, así que se negocia casi por puro diferencial de tipos y sentimiento — los ingredientes perfectos para movimientos grandes."),
            ("¿Qué es el carry trade en GBP/JPY?",
             "Pedir prestados yenes a tipos japoneses casi nulos e invertirlos en libras a tipos británicos más altos, embolsándose la diferencia. Da beneficios mientras los mercados están tranquilos y castiga cuando no lo están: en los episodios de huida del riesgo el yen se dispara al deshacerse las posiciones de carry, con frecuencia un 10 % o más frente a la libra en cuestión de meses."),
        ],
    },
    # ───────────────────────── AUD → JPY ────────────────────────
    "AUD-JPY": {
        "title": "AUD a JPY — Tipo de cambio, conversor y tablas",
        "description": "Convierte dólares australianos a yenes japoneses con tipos en vivo: el tipo de cambio AUD/JPY de hoy, una calculadora gratuita y qué mueve a este barómetro de riesgo.",
        "h1": "AUD a JPY — convertir dólares australianos a yenes japoneses",
        "intro": [
            "AUD/JPY es el barómetro de riesgo más puro del mercado de divisas. El dólar australiano representa el crecimiento global y la demanda de materias primas —ante todo la demanda industrial china—, mientras que el yen representa la seguridad. Cuando la economía mundial se expande, el par sube; cuando llega el pánico, cae más rápido que casi cualquier otro cruce importante.",
            "Es también el par clásico del carry trade: durante décadas los inversores pidieron prestados yenes baratos para comprar aussies de mayor rendimiento. Ese flujo moldea las largas tendencias alcistas del par y sus violentos episodios de liquidación — 2008 sigue siendo la historia ejemplar, cuando AUD/JPY perdió cerca de la mitad de su valor en unos pocos meses.",
        ],
        "faq": [
            ("¿Por qué los operadores llaman a AUD/JPY un barómetro de riesgo?",
             "Porque cada moneda ocupa un polo opuesto: el aussie sube con el crecimiento global y la demanda de materias primas, el yen sube con el miedo. El par se mueve, por tanto, con las bolsas mundiales en un grado que pocos cruces igualan — cuando cae con fuerza, la huida del riesgo es real."),
            ("¿Qué le pasó a AUD/JPY en la crisis de 2008?",
             "Quedó más o menos a la mitad. El carry trade se deshizo cuando el crédito global se congeló: los inversores vendieron dólares australianos para devolver los yenes prestados, y el par se hundió desde niveles superiores a 100 hasta los bajos 50 en cuestión de meses. Sigue siendo el ejemplo estándar de lo rápido que se invierten las estrategias de carry."),
        ],
    },
}
