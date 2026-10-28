# Mental Salus · Site institucional

Site estático (HTML e CSS, sem dependências) com a identidade visual de outubro de 2026.

## Estrutura

- `src/page.html`: fonte única do conteúdo e dos estilos.
- `build.py`: gera `index.html` (site publicado, com SEO) e `preview.html` (prévia no Claude).
- `assets/`: logo das folhas e ícone.
- `robots.txt` e `sitemap.xml`.

Depois de editar `src/page.html`, rode `python3 build.py`.

## Antes de publicar

No fim de `src/page.html`, preencher o bloco `CONFIG`:

- `whatsapp`: número com DDI e DDD, só dígitos (ex.: 5551999999999);
- `instagram` e `linkedin`: endereços completos dos perfis;
- `plataforma`: endereço da plataforma quando estiver no ar.

Campos vazios fazem os botões levarem ao formulário de contato.

## Publicação e domínio

1. Hospedagem gratuita: GitHub Pages (repositório público), Cloudflare Pages ou Netlify, conectados a este repositório.
2. Na hospedagem, configurar o domínio `www.mentalsalus.com.br` e redirecionar `mentalsalus.com.br` para ele.
3. No painel onde o domínio está registrado (Wix ou Registro.br), trocar apenas os registros do site (A/CNAME). **Não alterar os registros MX**, para não interromper o e-mail contato@mentalsalus.com.br.
4. Só cancelar o plano do Wix depois que o novo site estiver no ar e o e-mail tiver sido testado.
