"""Gera o site e a prévia.

Site (GitHub Pages, domínio próprio):
  index.html             página principal
  pro-gestao/index.html  página Pró-Gestão RPPS (endereço /pro-gestao/)
Prévia (página do Claude):
  preview.html           página principal
  preview-pro-gestao.html  publicada como pro-gestao.html junto da prévia

Fontes: src/page.html (head compartilhado + corpo da principal) e src/pro-gestao.html
(estilos próprios + corpo). Marcadores: {{PG}} link para a página Pró-Gestão,
{{HOME}} página inicial, {{R}} raiz dos arquivos em assets/.
"""
src = open('src/page.html', encoding='utf-8').read()
head, body = src.split('<!--BODY-->', 1)
pg_css, pg_body = open('src/pro-gestao.html', encoding='utf-8').read().split('<!--BODY-->', 1)

SITE = 'https://www.mentalsalus.com.br/'
ORG = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"Organization",'
       '"name":"Mental Salus Educação e Assessoria em Saúde","alternateName":"Mental Salus","url":"' + SITE + '",'
       '"logo":"' + SITE + 'assets/folhas.png","email":"contato@mentalsalus.com.br","areaServed":"BR",'
       '"telephone":"+55-51-99182-6563","sameAs":["https://www.instagram.com/mentalsalus/"],'
       '"address":{"@type":"PostalAddress","streetAddress":"Rua Mostardeiro, 157, sala 1402",'
       '"addressLocality":"Porto Alegre","addressRegion":"RS","postalCode":"90430-010","addressCountry":"BR"}}</script>\n')


def seo(desc, url, og_title, og_desc, icon_root, extra=''):
    return ('<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            '<meta name="description" content="' + desc + '">\n'
            '<meta name="theme-color" content="#FCFBF7">\n'
            '<link rel="canonical" href="' + url + '">\n'
            '<link rel="icon" type="image/png" href="' + icon_root + 'assets/favicon.png">\n'
            '<meta property="og:type" content="website">\n'
            '<meta property="og:locale" content="pt_BR">\n'
            '<meta property="og:title" content="' + og_title + '">\n'
            '<meta property="og:description" content="' + og_desc + '">\n'
            '<meta property="og:url" content="' + url + '">\n'
            '<meta property="og:image" content="' + SITE + 'assets/folhas.png">\n' + extra)


def doc(head_html, body_html):
    return '<!doctype html>\n<html lang="pt-BR">\n<head>\n' + head_html + '</head>\n<body>\n' + body_html + '</body>\n</html>\n'


site_head = head.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')

# Página principal
main_title = '<title>Mental Salus | Saúde mental e longevidade laboral no serviço público</title>'
main_seo = seo('Saúde mental e longevidade laboral no serviço público. Palestras, programas, consultoria e plataforma digital para RPPS, prefeituras e servidores, integrando saúde mental, física e financeira.',
               SITE, 'Mental Salus | A aposentadoria começa agora',
               'Saúde mental e longevidade laboral no serviço público, do ingresso ao pós-carreira.', '', ORG)
open('index.html', 'w', encoding='utf-8').write(
    doc(main_seo + site_head.replace('<title>Mental Salus</title>', main_title), body.replace('{{PG}}', 'pro-gestao/')))
open('preview.html', 'w', encoding='utf-8').write(head + body.replace('{{PG}}', 'pro-gestao.html'))

# Página Pró-Gestão
pg_title = '<title>Pró-Gestão RPPS | Mental Salus</title>'
pg_desc = ('Como o trabalho da Mental Salus em saúde do servidor, educação previdenciária e preparação para a '
           'aposentadoria contribui para ações do Pró-Gestão RPPS.')
pg_seo = seo(pg_desc, SITE + 'pro-gestao/', 'Pró-Gestão RPPS | Mental Salus', pg_desc, '/', ORG)
open('pro-gestao/index.html', 'w', encoding='utf-8').write(doc(
    pg_seo + site_head.replace('<title>Mental Salus</title>', pg_title) + pg_css,
    pg_body.replace('{{HOME}}', '/').replace('{{R}}', '/')))
prev_head = head.replace('<title>Mental Salus</title>', pg_title)
open('preview-pro-gestao.html', 'w', encoding='utf-8').write(doc(
    '<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n' + prev_head + pg_css,
    pg_body.replace('{{HOME}}', './').replace('{{R}}', '')))
print('ok')
