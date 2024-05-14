
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="collapsed", menu_items=None)



margins_css = """
    <style>
        .main > div {
            padding-left: 30rem;
            padding-right: 0rem;
        }
    </style>
"""

st.markdown(margins_css, unsafe_allow_html=True)


#components.iframe("https://eu-west-1.quicksight.aws.amazon.com/embed/8eea453c63104f6c9c4ee5043410b282/dashboards/b5b90e0c-8f84-4f48-9694-0332ff6244e0?isauthcode=true&identityprovider=quicksight&code=AYABeLsD4pMvpRVikZ5zADpqQswAAAABAAdhd3Mta21zAEthcm46YXdzOmttczpldS13ZXN0LTE6MzU2MzA1MTgzMDczOmtleS83ZTYwMTNkMC0xM2I0LTRmODItYmI1NC00YjllMTM4NzczNjYAuAECAQB4IZt0zcr71c1qotPywu6knKQF9RerzWvIw9ebvDgZ4T0BVkLCN-GSQVmNGuIIB9iz0gAAAH4wfAYJKoZIhvcNAQcGoG8wbQIBADBoBgkqhkiG9w0BBwEwHgYJYIZIAWUDBAEuMBEEDLhi4KL2-KmOtAha7gIBEIA7Umv5-phrcAWBL3UNG7qU4whmGuu0ZJ_BIS7pQPgAa-KYUpaN4VmdQpnDqmQuQdxK3Uf_NL9o8FMb5EwCAAAAAAwAABAAAAAAAAAAAAAAAAAAVtD6ntFVykx9PziJ4qSZeP____8AAAABAAAAAAAAAAAAAAABAAAAnvVrh7cMpnAeuL9NMbs-EWSXkHbclhj844StSfxaKGTMLD6cR_IJGEm1TXJYbHKe_ytDjooaAQzZt6iq2UxuQDihFKKp7pheW_8FnTPNWn7522gW-XKseDi5qmjbRQTi3jsgCvDteGWjBR-D0usSLzh_GmbFuJ-AnSDyUGzWzuVv1jMvxoD6mNiecpOwlGgYOPWrZxYv-aiIvdkr0osUv6vVv_qAh_fnjrpD56FrVA%3D%3D",scrolling=True,height=700)
#st.markdown(twitterLink, unsafe_allow_html=True)

st.markdown('''
    <style>
        #mostraIframeImage {
            position: fixed;
            bottom: 10px;
            right: 10px;
            width: 100px; /* Imposta la larghezza desiderata */
            height: 40px; /* Imposta l'altezza desiderata */
            cursor: pointer; /* Mostra il cursore come un puntatore quando passi sopra l'immagine */
            z-index: 9999; /* Assicura che l'immagine sia sopra tutti gli altri elementi */
            background-image: url('sirio_col.png'); /* Imposta l'immagine di sfondo */
            background-size: contain; /* Adatta l'immagine per coprire completamente il contenitore */
            background-repeat: no-repeat; /* Evita la ripetizione dell'immagine */
            background-position: center; /* Centra l'immagine all'interno del contenitore */
            overflow: hidden; /* Nasconde il contenuto testuale eccedente */
            text-indent: -9999px; /* Posiziona il testo al di fuori dell'area visibile */
        }

        #iframeContainer {
            display: none; /* Nascondi l'iframe all'inizio */
            position: fixed;
			top: 93%;
            left: 71%;
			right: 200%;
			bottom: 100%;
            transform: translate(-5%, -50%);
            width: 300px; /* Imposta la larghezza iniziale */
            height: 200px; /* Imposta l'altezza iniziale */
            z-index: 9998; /* Assicura che l'iframe sia sopra tutti gli altri elementi tranne l'immagine */
        }

        #iframeContainer.expanded {
			display:  block;
			position: fixed;
            width: 200%; /* Imposta la larghezza espansa */
            height: 200%; /* Imposta l'altezza espansa */
            max-width: 200px; /* Imposta la larghezza massima */
            max-height: 800px; /* Imposta l'altezza massima */
        }
		
		h1 {
    text-align: center; /* Centra il testo del titolo */
    font-family: 'Work Sans', normal; /* Modifica il tipo di carattere */
    color: #333; /* Cambia il colore del testo */
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* Aggiungi un'ombra al testo */
    margin-top: 50px; /* Aggiungi un margine superiore per lo spazio */
    
}
@media only screen and (max-width: 2600px) {
    #iframeContainer {
        display: none; /* Nascondi l'iframe all'inizio */
        position: fixed;
        top: 86%;
        left: 78%;
        right: 200%;
        bottom: 100%;
        transform: translate(-5%, -50%);
        width: 500px; /* Imposta la larghezza iniziale */
        height: 1000px; /* Imposta l'altezza iniziale */
        z-index: 9998; /* Assicura che l'iframe sia sopra tutti gli altri elementi tranne l'immagine */
        
    }
    #iframeContainer.expanded {
        display:  block;
        position: fixed;
        width: 200%; /* Imposta la larghezza espansa */
        height: 100%; /* Imposta l'altezza espansa */
        max-width: 500px; /* Imposta la larghezza massima */
        max-height: 700px; /* Imposta l'altezza massima */
    }
    .AleClass{
        height:50%;  
        min-height: 1920px;
		width:80%;
		min-width:800px;
    }
}

@media only screen and (max-width: 1920px) {
    #iframeContainer {
        display: none; /* Nascondi l'iframe all'inizio */
        position: fixed;
        top: 86%;
        left: 75%;
        right: 200%;
        bottom: 100%;
        transform: translate(-5%, -50%);
        max-width: 500px; /* Imposta la larghezza iniziale */
        max-height: 700px; /* Imposta l'altezza iniziale */
        z-index: 9998; /* Assicura che l'iframe sia sopra tutti gli altri elementi tranne l'immagine */
    }
    .AleClass{
        height:100%;  
        min-height: 400px;
	width:100%;
	min-width: 400px;
    }
    
}

@media only screen and (max-width: 1750px) {
    #iframeContainer {
        display: none; /* Nascondi l'iframe all'inizio */
        position: fixed;
        top: 86%;
        left: 70%;
        right: 200%;
        bottom: 100%;
        transform: translate(-5%, -50%);
        max-width: 500px; /* Imposta la larghezza iniziale */
        max-height: 700px; /* Imposta l'altezza iniziale */
        z-index: 9998; /* Assicura che l'iframe sia sopra tutti gli altri elementi tranne l'immagine */
    }
    .AleClass{
        height:50%;  
        max-height: 400px;
		width:50%;
		min-width: 400px;
    }
    
}

@media only screen and (max-width: 1550px) {
    #iframeContainer {
        display: none; /* Nascondi l'iframe all'inizio */
        position: fixed;
        top: 86%;
        left: 65%;
        right: 200%;
        bottom: 100%;
        transform: translate(-5%, -50%);
        max-width: 500px; /* Imposta la larghezza iniziale */
        max-height: 700px; /* Imposta l'altezza iniziale */
        z-index: 9998; /* Assicura che l'iframe sia sopra tutti gli altri elementi tranne l'immagine */
    }
    .AleClass{
        height:100%;  
        max-height: 400px;
		width:100%;
		min-width: 400px;
    }
    
}

@media only screen and (max-width: 1250px) {
    #iframeContainer {
        display: none; /* Nascondi l'iframe all'inizio */
        position: fixed;
        top: 90%;
        left: 25%;
        right: 200%;
        bottom: 100%;
        transform: translate(-5%, -50%);
        width: 300px; /* Imposta la larghezza iniziale */
        height: 200px; /* Imposta l'altezza iniziale */
        z-index: 9998; /* Assicura che l'iframe sia sopra tutti gli altri elementi tranne l'immagine */
    }
    .AleClass{
        height:100%;  
        max-height: 400px;
		width:100%;
		min-width:600px;
    }
    
}
@media only screen and (max-width: 768px) {
    #iframeContainer {
        display: none; /* Nascondi l'iframe all'inizio */
        position: fixed;
        top: 85%;
        left: 35%;
        right: 200%;
        bottom: 100%;
        transform: translate(-5%, -50%);
        width: 300px; /* Imposta la larghezza iniziale */
        height: 200px; /* Imposta l'altezza iniziale */
        z-index: 9998; /* Assicura che l'iframe sia sopra tutti gli altri elementi tranne l'immagine */
    }
    .AleClass{
        height:100%;  
        max-height: 400px;
		width:100%;
		min-width:250px;
    }
    
}


@media only screen and (max-width: 576px) {
    #iframeContainer {
        display: none; /* Nascondi l'iframe all'inizio */
        position: fixed;
        top: 85%;
        left: 27%;
        right: 200%;
        bottom: 100%;
        transform: translate(-5%, -50%);
        width: 200px; /* Imposta la larghezza iniziale */
        height: 200px; /* Imposta l'altezza iniziale */
        z-index: 9998; /* Assicura che l'iframe sia sopra tutti gli altri elementi tranne l'immagine */
    }
    .AleClass{
        height:100%;  
        max-height: 400px;
		width:85%;
		min-width:200px;
    }

@media only screen and (max-width: 450px) {
    #iframeContainer {
        display: none; /* Nascondi l'iframe all'inizio */
        position: fixed;
        top: 86%;
        left: 75%;
        right: 200%;
        bottom: 100%;
        transform: translate(-5%, -50%);
        max-width: 500px; /* Imposta la larghezza iniziale */
        max-height: 700px; /* Imposta l'altezza iniziale */
        z-index: 9998; /* Assicura che l'iframe sia sopra tutti gli altri elementi tranne l'immagine */
    }
    .AleClass{
        height:100%;  
        max-height: 400px;
		width:100%;
		min-width: 200px;
    }
    
}
}
@media only screen and (max-width: 450px) and (max-width:900px) {
    #iframeContainer {
        display: none; /* Nascondi l'iframe all'inizio */
        position: fixed;
        top: 90%;
        left: 10%;
        right: 200%;
        bottom: 100%;
        transform: translate(-5%, -50%);
        width: 300px; /* Imposta la larghezza iniziale */
        height: 300px; /* Imposta l'altezza iniziale */
        z-index: 9998; /* Assicura che l'iframe sia sopra tutti gli altri elementi tranne l'immagine */
    }
    .AleClass{
        height:100%;  
        max-height: 400px;
		width:300%;
		max-width:350px;
    }
    
}
@media only screen and (min-width: 850px) and (max-width:1300px) {
    #iframeContainer {
        display: none; /* Nascondi l'iframe all'inizio */
        position: fixed;
        top: 80%;
        left: 30%;
        right: 200%;
        bottom: 100%;
        transform: translate(-5%, -50%);
        width: 300px; /* Imposta la larghezza iniziale */
        height: 600px; /* Imposta l'altezza iniziale */
        z-index: 9998; /* Assicura che l'iframe sia sopra tutti gli altri elementi tranne l'immagine */
    }
    .AleClass{
        height:100%;  
        max-height: 500px;
		width:300%;
		max-width:600px;
    }
    
}

@media only screen and (min-width: 900px) and (max-width:1300px) {
    #iframeContainer {
        display: none; /* Nascondi l'iframe all'inizio */
        position: fixed;
        top: 80%;
        left: 30%;
        right: 200%;
        bottom: 100%;
        transform: translate(-5%, -50%);
        width: 300px; /* Imposta la larghezza iniziale */
        height: 600px; /* Imposta l'altezza iniziale */
        z-index: 9998; /* Assicura che l'iframe sia sopra tutti gli altri elementi tranne l'immagine */
    }
    .AleClass{
        height:100%;  
        max-height: 500px;
		width:300%;
		max-width:600px;
    }
    
}

@media only screen and (max-width: 400px) and (max-width:820px) {
    #iframeContainer {
        display: none; /* Nascondi l'iframe all'inizio */
        position: fixed;
        top: 80%;
        left: 10%;
        right: 200%;
        bottom: 100%;
        transform: translate(-5%, -50%);
        width: 300px; /* Imposta la larghezza iniziale */
        height: 300px; /* Imposta l'altezza iniziale */
        z-index: 9998; /* Assicura che l'iframe sia sopra tutti gli altri elementi tranne l'immagine */
    }
    .AleClass{
        height:100%;  
        max-height: 400px;
		width:300%;
		max-width:350px;
    }
    
}


    </style>
</head>

<script type='module' src='https://eu-central-1.quicksight.aws.amazon.com/embed/3e7883cb3ecc463ab1c79f5dc63608cd/dashboards/c46f86d1-ff0c-4d46-a436-f7d0fc5f1753?isauthcode=true&identityprovider=quicksight&code=AYABeLElUWZKPXqr_Jag3cxbY8EAAAABAAdhd3Mta21zAE5hcm46YXdzOmttczpldS1jZW50cmFsLTE6NjI5OTIyMjM1NDQ1OmtleS83NzZjMTM3ZS1hMzg0LTQ5YWUtOWM5Zi05N2Y2MWEyMzliMTMAuAECAQB4upFblB44WhL_YWcqJF2qJIDAY6Fc20C5K0Vg43hkghsBP_-M8ud-795yWXwjuqu_gQAAAH4wfAYJKoZIhvcNAQcGoG8wbQIBADBoBgkqhkiG9w0BBwEwHgYJYIZIAWUDBAEuMBEEDLhyD4iheRAm3MiXNgIBEIA7pAtcd-9AFalBZ1hXGudUlHpb3w2uXBfnwDlz1fKWTduYzKPUIXgkhTYte6Kw1yX19SUoXt1hKUGHMHwCAAAAAAwAABAAAAAAAAAAAAAAAAAAoIUWO1qJowdSYDU1ZJ-Spf____8AAAABAAAAAAAAAAAAAAABAAAAnnImzImi2PbzfH3Fv3R5kjdXgV0Z6y3obuYhKODkYcCVsLamuOOf21Ijm5ubUs8nxBrAvtWE6Ic6f_mumJku-egntxbUCU_bVtXJbhtyuzxO5oUP0MdDJd9Xr62SCx5r1j-Yr9jvoQ49TOA4U2r52MuFL6BJ_ddOdT6HxDKR930lzh2WAK4yJnzQDl0C8Q_ilY5o-tflB1FLWC0JlvA3QoBFGQR0Q6rGCTEBYuTMAw%3D%3D' width='2706' height='1033' hide-tabs toolbar='bottom' ></tableau-viz>
''',unsafe_allow_html=True)
