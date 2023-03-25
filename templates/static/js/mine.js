const contador = document.querySelector('.contador');
const link = document.querySelector('.container>div a:nth-of-type(1)');
const quadrados = document.querySelector('.quadrados');
const titulo = document.querySelector('.container>div h2');


function shuffle(array) {
    var m = array.length, t, i;

    while (m) {
        i = Math.floor(Math.random() * m--);

        t = array[m];
        array[m] = array[i];
        array[i] = t;
    }

    return array;
}
let numeros = [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0];

document.addEventListener('click', e => {

    const el = e.target;

    if (el == contador) {
        e.preventDefault();

        const horaAnteriorJSON = localStorage.getItem('hora_anterior');
        const horaAnterior = JSON.parse(horaAnteriorJSON);

        const horaAtual = new Date();
        const opcoes = {
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit',
            hour12: false,
        }
        const horaPosterior = horaAtual.toLocaleTimeString('pt-BR', opcoes);

        console.log(horaAnterior);
        console.log(horaPosterior);

        if(!horaAnterior){
            link.classList.add('mostrar');
            titulo.classList.add('mostrar');
            quadrados.innerHTML = '';
            aleatoriedade();
        } else{
            let horaA = horaAnterior.substring(0, 2);
            let minutoA = horaAnterior.substring(3, 5);
            let segundoA = horaAnterior.substring(6, 8);

            let horaP = horaPosterior.substring(0, 2);
            let minutoP = horaPosterior.substring(3, 5);
            let segundoP = horaPosterior.substring(6, 8);

            console.log(horaA, minutoA, segundoA);
            console.log(horaP, minutoP, segundoP);
            //14:30:45    15:10:10
            //14:31:46    15:11:11

            if(horaA == horaP && parseInt(minutoA) == parseInt(minutoP)){
                contador.innerHTML = 'Espere 1min';
            } else if(horaA == horaP && parseInt(minutoA) + 1 == parseInt(minutoP)
            && parseInt(segundoP) > parseInt(segundoA)){
                contador.innerHTML = 'Espere 1min';
            } else{
                link.classList.add('mostrar');
                titulo.classList.add('mostrar');
                quadrados.innerHTML = '';
                aleatoriedade();
            }
            
        }
    }

});


function aleatoriedade() {
    for (let i = 0; i < 10; i++) {
        numeros = shuffle(numeros)
    }

    setTimeout(function () {
        for (let i of numeros) {
            if (i == 0) {
                const imagemStar = document.createElement('img');
                imagemStar.setAttribute('src', "/static/images/star.png");

                const divStar = document.createElement('div');
                divStar.setAttribute('class', 'quadrado star');
                divStar.appendChild(imagemStar);

                quadrados.appendChild(divStar);
            } else {
                const imagemBomb = document.createElement('img');
                imagemBomb.setAttribute('src', "/static/images/bomb.png");

                const divBomb = document.createElement('div');
                divBomb.setAttribute('class', 'quadrado');
                divBomb.appendChild(imagemBomb);

                quadrados.appendChild(divBomb);
            }
        }
    }, 1);

    const data = new Date();
    const opcoes = {
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: false,
    }

    const elementoJSON = JSON.stringify(data.toLocaleTimeString('pt-BR', opcoes))
    localStorage.setItem('hora_anterior', elementoJSON)

    contador.innerHTML = '01:00';
    var interval;
    setTimeout(function () {
        let count = 59;
        interval = setInterval(function () {
            let formatacao = `${count}`.length == 2 ? `${count}` : '0' + count;
            contador.innerHTML = '00:' + formatacao;
            if (count == 0) {
                contador.innerHTML = 'Gerar Hack';
                quadrados.innerHTML = '';
                for (let i = 0; i < 25; i++) {
                    const divNormal = document.createElement('div');
                    divNormal.setAttribute('class', 'quadrado');
                    const divSpan = document.createElement('span');
                    divNormal.appendChild(divSpan);
                    quadrados.appendChild(divNormal);
                }
                link.classList.remove('mostrar');
                titulo.classList.remove('mostrar');
                clearInterval(interval);
            }
            count--;
        }, 1000)
    }, 1)
}



