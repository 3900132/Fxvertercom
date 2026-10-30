# -*- coding: utf-8 -*-
"""Conteúdos em português do Brasil para as páginas de pares de moedas
("USD para EUR").

PAIR_UI_L10N corresponde às strings de pair_pages.PAIR_UI["en"] (os
marcadores {f} {t} {d} permanecem intactos). PAIR_CONTENT_L10N corresponde
aos 15 pares de PAIR_CONTENT["en"], com chaves idênticas à versão inglesa.
build-lang-pages.py mescla ambos em PAIR_UI / PAIR_CONTENT.
"""

PAIR_UI_L10N = {
    "pairConvert": "Conversor ao vivo",
    "pairRateHead": "Taxa de câmbio atual",
    "pairAsOf": "Taxa de referência de {d}. O conversor ao vivo acima busca sempre a taxa mais recente — as tabelas abaixo são um retrato do momento da geração, apenas para orientação.",
    "pairAmounts": "Valores comuns: {f} para {t}",
    "pairReverse": "Valores comuns: {t} para {f}",
    "pairMore": "Mais conversões de {f}",
    "pairMorePairs": "Mais pares de moedas",
    "pairIntroHead": "Sobre a taxa de câmbio de {f} para {t}",
    "pairCurLinks": "Páginas de moedas",
    "pairMetaTmpl": ("Converta {f} para {t} com taxas de câmbio ao vivo: a taxa {f}/{t} de hoje, uma calculadora gratuita, "
                     "tabelas de valores comuns e o que move este par de moedas."),
}

PAIR_CONTENT_L10N = {
    # ───────────────────────── USD → EUR ─────────────────────────
    "USD-EUR": {
        "title": "USD para EUR — Taxa de câmbio, conversor e tabelas",
        "description": "Converta dólares americanos em euros com taxas ao vivo: a taxa de câmbio USD/EUR de hoje, uma calculadora gratuita, tabelas de valores comuns e o que move o par.",
        "h1": "USD para EUR — converter dólares americanos em euros",
        "intro": [
            "USD/EUR é o par de moedas mais negociado do mundo — cerca de um quarto de todo o volume do câmbio —, e é por isso que tem os spreads mais apertados e o mercado mais profundo de qualquer conversão. A taxa é simplesmente o preço de um dólar americano em euros, definido continuamente pelo comércio global, pelos fluxos de investimento e pela diferença de juros entre o Federal Reserve e o Banco Central Europeu.",
            "Para conversões do dia a dia, a pergunta prática é quanto de margem você está pagando sobre a taxa média de mercado exibida aqui. Bancos costumam acrescentar de 1% a 4%; cartões e serviços de transferência variam bastante. Conferir a taxa ao vivo antes de uma compra ou transferência mostra na hora se uma cotação é justa.",
        ],
        "faq": [
            ("Como a taxa de câmbio de USD para EUR é definida?",
             "Ela flutua livremente — a oferta e a demanda pelas duas moedas definem o preço 24 horas por dia, influenciadas principalmente pela política de juros do Fed e do BCE, pela inflação nos dois lados do Atlântico e pelo humor global de risco. Não há meta fixa nem administrada."),
            ("Qual é o melhor momento para converter USD para EUR?",
             "A liquidez é maior e os spreads, mais apertados, na sobreposição dos horários de negociação europeu e americano (aproximadamente das 13h às 17h UTC). Ninguém consegue prever com segurança a direção de curto prazo; para valores altos, é mais seguro converter em parcelas do que esperar um dia melhor."),
        ],
    },
    # ───────────────────────── USD → GBP ─────────────────────────
    "USD-GBP": {
        "title": "USD para GBP — Taxa de câmbio, conversor e tabelas",
        "description": "Converta dólares americanos em libras esterlinas com taxas ao vivo: a taxa de câmbio USD/GBP de hoje, uma calculadora gratuita, tabelas de valores e o que move a libra.",
        "h1": "USD para GBP — converter dólares americanos em libras esterlinas",
        "intro": [
            "A taxa entre o dólar e a libra, apelidada de “cable” pelo cabo telegráfico transatlântico que a transmitiu pela primeira vez nos anos 1860, é uma das cotações mais antigas do mundo em publicação contínua. Hoje ela reflete a diferença de juros entre o Federal Reserve e o Bank of England, a inflação britânica e a saúde do comércio e das contas públicas do Reino Unido.",
            "A libra negocia com mais intensidade durante o horário de Londres, e o par tende a dar saltos bruscos em volta de dados econômicos e anúncios fiscais do Reino Unido. Comparar qualquer cotação com a taxa média de mercado abaixo é o jeito mais rápido de ver quanta margem o provedor está levando.",
        ],
        "faq": [
            ("Por que a libra esterlina vale mais que o dólar americano?",
             "Preço unitário maior não significa economia mais forte — reflete a história e as denominações. A libra era a moeda dominante do mundo quando o dólar ainda não existia; o número em si não diz nada sobre a força econômica relativa nem sobre o poder de compra."),
            ("O que mais move o USD/GBP?",
             "Decisões de juros do Fed e do Bank of England, dados de inflação britânicos e notícias políticas e fiscais de Westminster. No voto do Brexit, em 2016, a libra caiu cerca de 10% em um dia — um lembrete de que a esterlina carrega um risco político que a maioria das moedas grandes não conhece."),
        ],
    },
    # ───────────────────────── USD → JPY ─────────────────────────
    "USD-JPY": {
        "title": "USD para JPY — Taxa de câmbio, conversor e tabelas",
        "description": "Converta dólares americanos em ienes japoneses com taxas ao vivo: a taxa de câmbio USD/JPY de hoje, uma calculadora gratuita, tabelas de valores e o que move o iene.",
        "h1": "USD para JPY — converter dólares americanos em ienes japoneses",
        "intro": [
            "USD/JPY é o segundo par de moedas mais negociado do mundo e o barômetro clássico da diferença de juros entre Estados Unidos e Japão. Como os juros japoneses ficaram perto de zero por décadas, o iene virou a moeda de financiamento favorita do mundo — ele se enfraquece quando os mercados estão confiantes e se fortalece com força quando as crises desmancham essas posições.",
            "O par também é observado de perto por causa das intervenções oficiais do Japão: o Ministério das Finanças já comprou ienes repetidamente quando ele caía demais, rápido demais. Conversões grandes valem ser conferidas contra a taxa média de mercado, porque as margens de varejo no JPY podem ser enganosamente largas.",
        ],
        "faq": [
            ("Por que o iene às vezes cai tanto contra o dólar?",
             "Principalmente por causa da diferença de juros. Quando os juros americanos estão altos e os japoneses seguem perto de zero, investidores vendem ienes para comprar ativos em dólares mais rentáveis — o carry trade. O iene pode deslizar por meses e depois saltar violentamente quando essas posições se desfazem."),
            ("O governo japonês pode mudar a taxa USD/JPY?",
             "Ele pode ir contra o mercado, não invertê-lo. O Japão já interveio comprando ou vendendo ienes quando os movimentos ficavam desordenados, às vezes com dezenas de bilhões de dólares em um único episódio. A intervenção suaviza o caminho; raramente muda a direção de longo prazo definida pelos fundamentos."),
        ],
    },
    # ───────────────────────── USD → CNY ─────────────────────────
    "USD-CNY": {
        "title": "USD para CNY — Taxa de câmbio, conversor e tabelas",
        "description": "Converta dólares americanos em yuans chineses com taxas ao vivo: a taxa de câmbio USD/CNY de hoje, uma calculadora gratuita, tabelas de valores e como funciona a taxa administrada.",
        "h1": "USD para CNY — converter dólares americanos em yuans chineses",
        "intro": [
            "A taxa entre o dólar e o yuan é o maior par de moedas administrado por um banco central. Todas as manhãs o People's Bank of China define um preço central diário, e a taxa onshore (CNY) só pode se mover dentro de uma banda ao redor dele — por isso o USD/CNY oscila muito menos no dia a dia do que sua importância econômica sugere.",
            "O superávit comercial da China, os controles de capital e os objetivos de política econômica moldam a taxa. Para conversões, saiba que o CNY onshore e o CNH offshore podem diferir um pouco, e que a conversão de moeda por indivíduos na China está sujeita a regras de controle de capital. Compare sempre as cotações com a taxa de referência abaixo.",
        ],
        "faq": [
            ("O yuan chinês é livremente conversível?",
             "Não totalmente. A conversão ligada ao comércio é fácil, mas os fluxos de investimento através da fronteira são controlados por cotas e aprovações. É por isso que a versão offshore (CNH) negocia a um preço um pouco diferente do CNY onshore — a diferença mostra o custo de mover dinheiro através da fronteira."),
            ("Por que o USD/CNY quase não se move comparado a outros pares?",
             "Porque o banco central o administra. O fixing diário e a banda de negociação mantêm a taxa estável em relação ao dólar, de acordo com a preferência da China por previsibilidade no comércio. Administrado não significa fixo: ao longo de meses e anos, a taxa acompanha os fundamentos."),
        ],
    },
    # ───────────────────────── USD → INR ─────────────────────────
    "USD-INR": {
        "title": "USD para INR — Taxa de câmbio, conversor e tabelas",
        "description": "Converta dólares americanos em rupias indianas com taxas ao vivo: a taxa de câmbio USD/INR de hoje, uma calculadora gratuita, tabelas de valores e o que move a rupia.",
        "h1": "USD para INR — converter dólares americanos em rupias indianas",
        "intro": [
            "USD/INR é um dos maiores corredores de remessas do mundo — a Índia recebe mais remessas do que qualquer outro país — e um par emergente muito negociado. O Reserve Bank of India administra a volatilidade, não o nível: suaviza movimentos bruscos com suas reservas, mas deixa a rupia encontrar sua tendência de longo prazo.",
            "A história de fundo da rupia é uma desvalorização gradual contra o dólar, movida pelos diferenciais de inflação e pela balança corrente da Índia, interrompida por episódios globais de risco. Para quem envia dinheiro à Índia, a diferença entre a taxa média de mercado e a taxa oferecida é onde o custo real se esconde.",
        ],
        "faq": [
            ("Por que a rupia indiana se desvaloriza com o tempo?",
             "Principalmente pelos diferenciais de inflação e pelo déficit comercial: a Índia importa muito mais do que exporta, e a diferença é financiada por entrada de capital. O RBI suaviza o caminho, mas ao longo de décadas a rupia se enfraqueceu de forma constante contra o dólar — o normal para uma economia em desenvolvimento."),
            ("Como conseguir a melhor taxa ao enviar dinheiro para a Índia?",
             "Compare a taxa oferecida com a taxa média de mercado antes de enviar, e não só as tarifas. Serviços especializados em remessas costumam superar as transferências bancárias nesse corredor, e uma diferença de até 1% é significativa em transferências familiares regulares ao longo de um ano."),
        ],
    },
    # ───────────────────────── USD → CAD ─────────────────────────
    "USD-CAD": {
        "title": "USD para CAD — Taxa de câmbio, conversor e tabelas",
        "description": "Converta dólares americanos em dólares canadenses com taxas ao vivo: a taxa de câmbio USD/CAD de hoje, uma calculadora gratuita, tabelas de valores e o que move o loonie.",
        "h1": "USD para CAD — converter dólares americanos em dólares canadenses",
        "intro": [
            "USD/CAD — o “loonie” — é um par do top cinco mundial, construído sobre uma das maiores relações comerciais do planeta. O Canadá envia cerca de três quartos das suas exportações para os Estados Unidos, então o par negocia fortemente o crescimento americano, os preços da energia (o Canadá é um grande exportador de petróleo) e a diferença de juros entre o Fed e o Bank of Canada.",
            "Quando o petróleo sobe, o CAD costuma se fortalecer; quando o medo pela economia global bate, ele enfraquece junto com as moedas de commodities em geral. O par é líquido a qualquer hora, e cotações a uma fração de ponto percentual da taxa média de mercado são fáceis de achar — margens largas sempre merecem desconfiança.",
        ],
        "faq": [
            ("Por que o dólar canadense se chama loonie?",
             "Pelo mergulhão (loon) gravado na moeda de um dólar lançada em 1987. O apelido pegou e hoje nomeia a própria moeda na gíria do câmbio, como em “o loonie se valorizou hoje”."),
            ("O preço do petróleo realmente afeta o USD/CAD?",
             "Sim, de forma visível. O petróleo bruto e derivados são a maior categoria de exportação do Canadá, então o petróleo em alta tende a trazer mais dólares para o país e a elevar o CAD. Operadores tratam o par como uma aposta aproximada nos mercados de energia, além dos juros dos dois países."),
        ],
    },
    # ───────────────────────── USD → AUD ─────────────────────────
    "USD-AUD": {
        "title": "USD para AUD — Taxa de câmbio, conversor e tabelas",
        "description": "Converta dólares americanos em dólares australianos com taxas ao vivo: a taxa de câmbio USD/AUD de hoje, uma calculadora gratuita, tabelas de valores e o que move o aussie.",
        "h1": "USD para AUD — converter dólares americanos em dólares australianos",
        "intro": [
            "O dólar australiano é a moeda de commodities por excelência: sua sorte acompanha as exportações de minério de ferro, carvão e gás e, acima de tudo, a demanda chinesa por eles. USD/AUD é, por isso, um dos indicadores em tempo real mais limpos do apetite global por risco — o aussie se fortalece quando o comércio mundial ferve e enfraquece nos episódios de fuga do risco.",
            "A política de juros do Reserve Bank of Australia e do Fed comanda os movimentos de curto prazo. As populações de estudantes e de intercambistas working holiday fazem de USD→AUD (e de volta) uma conversão recorrente, na qual até uma margem de 1% se acumula rápido.",
        ],
        "faq": [
            ("Por que o dólar australiano é tão sensível à China?",
             "A China é o maior mercado de exportação da Austrália com folga, sobretudo de minério de ferro para a siderurgia. Quando a construção chinesa desacelera, os preços das commodities e o AUD costumam cair juntos — a moeda funciona como um barômetro em tempo real da indústria pesada chinesa."),
            ("O AUD é um porto seguro?",
             "O oposto: operadores o chamam de moeda de risco. Nos pânicos globais — 2008, 2020 — o dinheiro corre para o dólar americano, e o aussie tende a cair mais que qualquer outra moeda grande. Essa ciclicidade é justamente o motivo de operadores de carry e observadores do crescimento vigiá-lo de perto."),
        ],
    },
    # ───────────────────────── USD → CHF ─────────────────────────
    "USD-CHF": {
        "title": "USD para CHF — Taxa de câmbio, conversor e tabelas",
        "description": "Converta dólares americanos em francos suíços com taxas ao vivo: a taxa de câmbio USD/CHF de hoje, uma calculadora gratuita, tabelas de valores e o que move o franco.",
        "h1": "USD para CHF — converter dólares americanos em francos suíços",
        "intro": [
            "O franco suíço é a grande moeda refúgio do mundo: quando guerra, estresse bancário ou pânico de mercado chegam, o dinheiro flui para a Suíça e o CHF se fortalece. USD/CHF tende, por isso, a cair nas crises globais mesmo quando o próprio dólar é um refúgio — o franco é simplesmente o abrigo mais forte.",
            "O Swiss National Bank molda a taxa de forma ativa, do famoso piso contra o euro de 2011–2015 às intervenções pesadas desde então. Para conversões, a Suíça também lembra que um par de país rico pode ter margens de varejo largas, sobretudo em aeroportos e hotéis — confira sempre a referência da taxa média de mercado.",
        ],
        "faq": [
            ("Por que o franco suíço é considerado um porto seguro?",
             "Um século de neutralidade, dívida baixa, superávit em conta corrente e um banco central crível fazem do franco o estacionamento padrão do dinheiro que foge do risco. A inflação suíça também correu por décadas bem abaixo da americana e da da zona do euro, preservando o poder de compra da moeda."),
            ("O que o SNB fez em janeiro de 2015?",
             "Abandonou de repente o teto à valorização do franco contra o euro. USD/CHF e EUR/CHF despencaram cerca de 20–30% em minutos — um dos maiores movimentos intradiários já vistos em um par grande, e a razão pela qual operadores ainda respeitam a expressão “risco SNB”."),
        ],
    },
    # ───────────────────────── USD → MXN ─────────────────────────
    "USD-MXN": {
        "title": "USD para MXN — Taxa de câmbio, conversor e tabelas",
        "description": "Converta dólares americanos em pesos mexicanos com taxas ao vivo: a taxa de câmbio USD/MXN de hoje, uma calculadora gratuita, tabelas de valores e o que move o peso.",
        "h1": "USD para MXN — converter dólares americanos em pesos mexicanos",
        "intro": [
            "USD/MXN é o par emergente mais negociado das Américas e um dos mais líquidos do mundo. O peso negocia tudo o que move a economia americana — política comercial, crescimento, diferença de juros entre o Fed e o Banxico —, além dos preços do petróleo e do enorme corredor de remessas vindo dos Estados Unidos.",
            "Por ser tão líquido, o par reage rápido ao humor global de risco: é um alvo clássico de carry trade que se fortalece em mercados calmos e dá saltos violentos nos pânicos. Para viajantes e remetentes, margens de 3% a 6% são comuns em aeroportos — a taxa média de mercado abaixo é a referência para comparar.",
        ],
        "faq": [
            ("Por que o USD/MXN é tão volátil?",
             "Os juros altos do México atraem dinheiro especulativo de curto prazo que sai rápido nos momentos de estresse; o peso também é o ativo de referência de todo o comércio e das notícias políticas entre EUA e México. A combinação o torna líquido, mas nervoso — movimentos diários grandes são o normal, não defeito."),
            ("Qual é o jeito mais barato de enviar dólares para o México?",
             "Serviços especializados em remessas batem consistentemente bancos e lojas de envio em dinheiro nesse corredor. Compare o valor entregue com a taxa média de mercado: numa transferência de 300 dólares, a diferença entre uma cotação justa e uma margem de 5% pode ser um dia inteiro de salário local."),
        ],
    },
    # ───────────────────────── USD → PHP ─────────────────────────
    "USD-PHP": {
        "title": "USD para PHP — Taxa de câmbio, conversor e tabelas",
        "description": "Converta dólares americanos em pesos filipinos com taxas ao vivo: a taxa de câmbio USD/PHP de hoje, uma calculadora gratuita, tabelas de valores e o que move o peso.",
        "h1": "USD para PHP — converter dólares americanos em pesos filipinos",
        "intro": [
            "O peso filipino se apoia em um dos maiores fluxos de remessas do mundo: milhões de trabalhadores filipinos no exterior enviam dinheiro para casa, e essas entradas de dólares são um pilar da economia. USD/PHP negocia, em consequência, o apetite global por risco, os preços do petróleo (as Filipinas são importadoras líquidas) e a política do Bangko Sentral ng Pilipinas.",
            "A taxa oficial é administrada com mão leve — o banco central permite o ajuste gradual enquanto suaviza picos. Para famílias de trabalhadores emigrados e viajantes, a dispersão entre provedores nesse corredor é ampla; conferir a taxa média de mercado antes de enviar é o jeito mais simples de economizar.",
        ],
        "faq": [
            ("Como as remessas afetam o peso filipino?",
             "As entradas constantes de dólares dos trabalhadores no exterior sustentam o peso e o balanço de pagamentos do país — vários pontos percentuais do PIB por ano. Quando o risco global sobe ou as economias de destino enfraquecem, as remessas minguam e o peso tende a seguir."),
            ("É melhor converter USD para PHP nos Estados Unidos ou nas Filipinas?",
             "Depende do provedor, não do país. Os dois lados do corredor têm opções baratas e caras; o número decisivo é quantos pesos o destinatário realmente recebe. Compare cotações contra a taxa média de mercado em vez de confiar na loja mais próxima."),
        ],
    },
    # ───────────────────────── EUR → GBP ────────────────────────
    "EUR-GBP": {
        "title": "EUR para GBP — Taxa de câmbio, conversor e tabelas",
        "description": "Converta euros em libras esterlinas com taxas ao vivo: a taxa de câmbio EUR/GBP de hoje, uma calculadora gratuita, tabelas de valores e o que move este par.",
        "h1": "EUR para GBP — converter euros em libras esterlinas",
        "intro": [
            "EUR/GBP é o clássico cruzamento europeu: duas economias que se enviam cerca de metade do comércio mútuo, separadas por uma única fronteira cambial. Como as duas são moedas desenvolvidas e de baixa inflação, o par se move bem menos que os cruzamentos com o dólar — no fundo, é uma aposta nas fortunas relativas da zona do euro e do Reino Unido.",
            "A diferença de juros entre o BCE e o Bank of England comanda a maior parte da tendência, enquanto notícias políticas e fiscais britânicas causam os picos. Para trabalhadores transfronteiriços, aposentados e empresas, a estabilidade do par faz pequenas diferenças de taxa importarem ainda mais: uma margem de 1% é uma fatia grande do movimento anual total.",
        ],
        "faq": [
            ("Por que o EUR/GBP é mais calmo que o EUR/USD?",
             "Nem o euro nem a libra são moedas globais de risco, então as grandes fugas para a segurança passam por cima deles. O par reflete sobretudo a economia relativa Reino Unido–UE e os diferenciais de juros, que mudam devagar — embora possa disparar com notícias políticas britânicas, como mostrou 2016."),
            ("Como o Brexit ainda afeta o EUR/GBP?",
             "Estruturalmente. As novas fricções comerciais desde 2021 tornaram a economia britânica um pouco menos aberta à UE, o que a maioria dos economistas liga a uma esterlina estruturalmente mais fraca. Cada rodada de negociações Reino Unido–UE sobre regras comerciais ainda move o par."),
        ],
    },
    # ───────────────────────── EUR → CHF ────────────────────────
    "EUR-CHF": {
        "title": "EUR para CHF — Taxa de câmbio, conversor e tabelas",
        "description": "Converta euros em francos suíços com taxas ao vivo: a taxa de câmbio EUR/CHF de hoje, uma calculadora gratuita, tabelas de valores e o papel do Swiss National Bank no par.",
        "h1": "EUR para CHF — converter euros em francos suíços",
        "intro": [
            "EUR/CHF é o teste de fogo refúgio da Europa: sempre que a tensão na zona do euro sobe — a crise da dívida de 2011, sustos bancários, guerra no continente — o dinheiro cruza a fronteira suíça e o par cai. O Swiss National Bank vigia essa taxa mais que qualquer outra e já interveio repetidamente para impedir que o franco sufocasse as exportações suíças.",
            "A história moderna do par é dramática: um piso em 1,20 desde 2011 e, depois, o desapego de janeiro de 2015, que produziu um flash crash de 20–30% em minutos. Desde então o franco negocia como um refúgio limpo, ainda que às vezes forte demais — e o SNB segue participante ativo desse mercado.",
        ],
        "faq": [
            ("Por que o Swiss National Bank se importa tanto com o EUR/CHF?",
             "Porque a economia suíça vende para a Europa. Um franco forte demais torna as exportações suíças pouco competitivas e arrasta a inflação abaixo da meta, então o SNB compra moeda estrangeira (e já impôs juros negativos) para limitar a força do franco. Ele intervém nesse par mais que quase qualquer outro banco central num mercado grande."),
            ("O EUR/CHF é um par estável para manter?",
             "É estável em tempos calmos e explosivo nas crises — o oposto de diversificado. O desapego de 2015 segue o aviso clássico de que a promessa de um banco central de segurar uma moeda pode ser retirada da noite para o dia. Quem tratou o par como sem risco aprendeu o contrário numa manhã."),
        ],
    },
    # ───────────────────────── EUR → PLN ────────────────────────
    "EUR-PLN": {
        "title": "EUR para PLN — Taxa de câmbio, conversor e tabelas",
        "description": "Converta euros em zlotis poloneses com taxas ao vivo: a taxa de câmbio EUR/PLN de hoje, uma calculadora gratuita, tabelas de valores e o que move o zloti.",
        "h1": "EUR para PLN — converter euros em zlotis poloneses",
        "intro": [
            "A Polônia é a sexta maior economia da União Europeia que ainda usa moeda própria, e o zloti é o mais negociado entre as moedas da UE fora do euro. EUR/PLN negocia a diferença de juros com o National Bank of Poland, os fundos da UE que fluem para o leste, os pedidos da indústria alemã à indústria polonesa e o risco geopolítico regional.",
            "Desde que a Polônia entrou na UE, em 2004, o zloti se fortaleceu nos booms e caiu com força nas crises — 2008 e 2022 levaram o par a extremos históricos. Com a eventual adoção do euro ainda indefinida, o par segue uma peça estrutural das finanças europeias por anos.",
        ],
        "faq": [
            ("A Polônia vai adotar o euro e eliminar o zloti?",
             "A Polônia é legalmente obrigada a adotar o euro mais cedo ou mais tarde, mas não tem data-alvo e o ceticismo público é amplo. Enquanto não houver um calendário crível de adoção, o EUR/PLN segue um par muito negociado — declarações políticas sobre o calendário já o movem sozinhas."),
            ("Por que o EUR/PLN disparou em 2022?",
             "A guerra na vizinha Ucrânia transformou a Polônia em economia de linha de frente da noite para o dia: entrada de refugiados, gasto com defesa e choques de energia golpearam a moeda. O National Bank of Poland interveio para sustentar o zloti — os movimentos mais bruscos do par em duas décadas."),
        ],
    },
    # ───────────────────────── GBP → JPY ────────────────────────
    "GBP-JPY": {
        "title": "GBP para JPY — Taxa de câmbio, conversor e tabelas",
        "description": "Converta libras esterlinas em ienes japoneses com taxas ao vivo: a taxa de câmbio GBP/JPY de hoje, uma calculadora gratuita, tabelas de valores e o que move este par volátil.",
        "h1": "GBP para JPY — converter libras esterlinas em ienes japoneses",
        "intro": [
            "GBP/JPY — os veteranos o chamavam de “a fera” ou “o dragão” — é um dos pares grandes mais voláteis. Ele empilha dois motores de risco: a sensibilidade da esterlina às notícias políticas e fiscais britânicas e o papel do iene como moeda de financiamento mundial, que o faz oscilar com força toda vez que o sentimento global vira.",
            "O par é o favorito do carry trade: pegar ienes emprestados a juros quase zero para comprar libras mais rentáveis. Funciona até uma crise obrigar todo mundo a sair ao mesmo tempo — por isso o GBP/JPY tende a subir em ritmo lento por anos e a cair violentamente em semanas. Tamanho e momento importam aqui mais que em quase qualquer outro par grande.",
        ],
        "faq": [
            ("Por que o GBP/JPY é mais volátil que o USD/JPY?",
             "Porque multiplica duas volatilidades. A esterlina acrescenta o risco político e econômico britânico sobre o sentimento global que já move o USD/JPY. O par não tem economia-âncora em comum, então negocia quase puro diferencial de juros e sentimento — receita para movimentos grandes."),
            ("O que é o carry trade no GBP/JPY?",
             "Pegar ienes emprestados a juros japoneses quase nulos e investir em libras a juros britânicos mais altos, embolsando a diferença. Dá lucro enquanto os mercados estão calmos e castiga quando não estão: nos episódios de fuga do risco, o iene dispara quando as posições de carry se desfazem, com frequência 10% ou mais contra a libra em questão de meses."),
        ],
    },
    # ───────────────────────── AUD → JPY ────────────────────────
    "AUD-JPY": {
        "title": "AUD para JPY — Taxa de câmbio, conversor e tabelas",
        "description": "Converta dólares australianos em ienes japoneses com taxas ao vivo: a taxa de câmbio AUD/JPY de hoje, uma calculadora gratuita, tabelas de valores e o que move este barômetro de risco.",
        "h1": "AUD para JPY — converter dólares australianos em ienes japoneses",
        "intro": [
            "AUD/JPY é o barômetro de risco mais puro do mercado de câmbio. O dólar australiano representa o crescimento global e a demanda por commodities — acima de tudo a demanda industrial chinesa —, enquanto o iene representa segurança. Quando a economia mundial se expande, o par sobe; quando o pânico chega, ele cai mais rápido que quase qualquer outro cruzamento grande.",
            "É também o par clássico do carry trade: por décadas, investidores pegaram ienes baratos emprestados para comprar aussies mais rentáveis. Esse fluxo molda as longas altas em ritmo lento do par e seus violentos episódios de desmontagem — 2008 segue a história de advertência, quando o AUD/JPY perdeu cerca de metade do valor em poucos meses.",
        ],
        "faq": [
            ("Por que operadores chamam o AUD/JPY de barômetro de risco?",
             "Porque cada moeda fica num polo oposto: o aussie sobe com o crescimento global e a demanda por commodities, o iene sobe com o medo. O par se move, portanto, junto com as bolsas mundiais num grau que poucos cruzamentos igualam — quando ele cai com força, a fuga do risco é real."),
            ("O que aconteceu com o AUD/JPY na crise de 2008?",
             "Caiu aproximadamente à metade. O carry trade se desfez quando o crédito global congelou: investidores venderam dólares australianos para pagar os ienes emprestados, e o par despencou de mais de 100 para os baixos 50 em poucos meses. Continua o exemplo padrão da velocidade com que estratégias de carry se invertem."),
        ],
    },
}
