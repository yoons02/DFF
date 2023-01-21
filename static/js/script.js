const password = document.getElementById('password')
const login = document.getElementById('login')

login.addEventListener('click', () => {
    if (password.value == '0000') {
            alert('로그인 되었습니다!')
        }
        else {
            alert('비밀번호를 다시 입력해주세요!')
        }
})
