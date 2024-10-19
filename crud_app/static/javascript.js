(function(win, doc){
    'use strict';

// exibe mensagem de confirmação ao excluir registro

    if(doc.querySelector('.btnDel')){
        let btnDel = doc.querySelectorAll('.btnDel');
        for(let i=0; i<btnDel.length; i++){
            btnDel[i].addEventListener('click', function(event){
                if(confirm('Confirma a exclusão do registro?')){
                    return true;
                }else{
                    event.preventDefault();
                }
            });
        }
    }

    // Ajax do formulário de cadastro/edição

    if(doc.querySelector('#form')){
        let form = doc.querySelector('#form');
        form.addEventListener('submit', function(event){
            event.preventDefault();
            let data = new FormData(form);
            let ajax = new XMLHttpRequest();
            let token = doc.querySelectorAll('input')[0].value;
            ajax.open('POST', form.action);
            ajax.setRequestHeader('X-CSRF-TOKEN', token);
            ajax.onreadystatechange = function()
            {
                if(ajax.status === 200 && ajax.readyState === 4){
                    console.log('Cadastro realizado com sucesso!');
                    let result = doc.querySelector('#result');
                    result.innerHTML = 'Cadastro realizado com sucesso!';
                    result.classList.add('alert');
                    result.classList.add('alert-success');
                }
            }
            ajax.send(data);
            form.reset();
        });
        form.addEventListener('submit', sendForm, false);
        }
})(window, document);