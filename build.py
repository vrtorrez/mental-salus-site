"""Gera index.html (site completo) e preview.html (prévia publicada como página do Claude)."""
src = open('src/page.html', encoding='utf-8').read()
head, body = src.split('<!--BODY-->', 1)
head_site = head.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
seo = '''<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Saúde mental e longevidade laboral no serviço público. Palestras, programas, consultoria e plataforma digital para RPPS, prefeituras e servidores, integrando saúde mental, física e financeira.">
<meta name="theme-color" content="#FCFBF7">
<link rel="canonical" href="https://www.mentalsalus.com.br/">
<link rel="icon" type="image/png" href="assets/favicon.png">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:title" content="Mental Salus | A aposentadoria começa agora">
<meta property="og:description" content="Saúde mental e longevidade laboral no serviço público, do ingresso ao pós-carreira.">
<meta property="og:url" content="https://www.mentalsalus.com.br/">
<meta property="og:image" content="https://www.mentalsalus.com.br/assets/folhas.png">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"Organization","name":"Mental Salus Educação e Assessoria em Saúde","alternateName":"Mental Salus","url":"https://www.mentalsalus.com.br/","logo":"https://www.mentalsalus.com.br/assets/folhas.png","email":"contato@mentalsalus.com.br","areaServed":"BR","telephone":"+55-51-99182-6563","sameAs":["https://www.instagram.com/mentalsalus/"],"address":{"@type":"PostalAddress","streetAddress":"Rua Mostardeiro, 157, sala 1402","addressLocality":"Porto Alegre","addressRegion":"RS","postalCode":"90430-010","addressCountry":"BR"}}</script>
'''
head_site = head_site.replace('<title>Mental Salus</title>', '<title>Mental Salus | Saúde mental e longevidade laboral no serviço público</title>')
site = '<!doctype html>\n<html lang="pt-BR">\n<head>\n' + seo + head_site + '</head>\n<body>\n' + body + '</body>\n</html>\n'
open('index.html', 'w', encoding='utf-8').write(site)
open('preview.html', 'w', encoding='utf-8').write(head + body)
print('ok', len(site))
