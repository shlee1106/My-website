document.addEventListener('DOMContentLoaded', () => {
  const repos = [
    { name: "My-website", url: "https://api.github.com/repos/shlee1106/My-website/contents/" },
    { name: "testcode", url: "https://api.github.com/repos/shlee1106/testcode/contents/" }
  ];

  const container = document.createElement('div');
  document.body.appendChild(container);

  repos.forEach(repo => {
    const section = document.createElement('section');
    const title = document.createElement('h2');
    title.textContent = repo.name;
    section.appendChild(title);

    const ul = document.createElement('ul');
    section.appendChild(ul);

    fetch(repo.url)
      .then(res => res.json())
      .then(data => {
        data.forEach(file => {
          const li = document.createElement('li');
          const a = document.createElement('a');
          a.href = file.html_url;
          a.textContent = file.name;
          a.target = "_blank"; // 새 탭에서 열기
          li.appendChild(a);
          ul.appendChild(li);
        });
      })
      .catch(err => console.error(err));

    container.appendChild(section);
  });
});

document.addEventListener('DOMContentLoaded', () => {
  const links = document.querySelectorAll('nav a');

  links.forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault(); // 기본 앵커 이동 막기
      const targetId = link.getAttribute('href').substring(1); // #home -> home
      document.getElementById(targetId).scrollIntoView({ behavior: 'smooth' });

      // 브라우저 히스토리에 추가
      history.pushState({ section: targetId }, '', `#${targetId}`);
    });
  });

  // 브라우저 뒤로가기/앞으로가기 처리
  window.addEventListener('popstate', (e) => {
    const targetId = e.state?.section || 'home';
    document.getElementById(targetId).scrollIntoView({ behavior: 'smooth' });
  });
});

