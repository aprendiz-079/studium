
declare -a estudos

function pegar_estudos
{
  local estudo
  while [ 1 ]
  do
    read -p 'Insira o estudo: ' estudo

    if [ -z "$estudo" ]
    then
      break
    fi
    estudos+=("$estudo")
  done
  return 0
}


function sortear
{
  local total_estudos=${#estudos[@]}
  local num=$((RANDOM % $total_estudos + 0))
  printf "%u" $num
}

function main
{
  pegar_estudos

  local indice_sorteado=$(sortear)
  local estudo_sorteado=${estudos[indice_sorteado]}

  echo -e "Estudo sorteado: $estudo_sorteado"
}

main
