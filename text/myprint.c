#include<stdio.h>
#include<stdarg.h>

int myprint(const char* string, ...);

int main(void)
{
    int a,b;

    a = printf("Hello world!\n");
    printf("%d,%s,%d\n", a, "Wow", 7031);
    b = myprint("Hello world!\n");
    myprint("%d,%s,%d\n", b, "Wow", 7031);

    return 0;
}

int myprint(const char* string, ...)
{
    va_list arg;
    char buffer[BUFSIZ];
    int temp = 0;

    char* p_string = NULL;
    char* p_temp   = NULL;
    char* p_buffer = buffer;

    int counter = 0;
    int number  = 0;
    int num_d   = 0;

    va_start(arg, string);

    for (counter = 0, p_string = string; *(p_string) != '\0';){
        switch(*p_string){
            case '%':
                p_string++;

                switch(*p_string){
                    case 'd':
                        temp = va_arg(arg, int);
                        num_d = temp;

                        while(num_d){
                            number++;
                            counter++;
                            num_d /= 10;
                        }

                        num_d = temp;

                        while(number){
                            *(p_buffer+number-1) = (num_d % 10);
                            num_d /= 10;
                            number--;
                        }

                        p_buffer += number;
                        break;

                    case 'c':
                        temp = va_arg(arg, int);
                        *(p_buffer++) = temp;
                        break;

                    case 's':
                        p_temp = va_arg(arg, char*);

                        while(p_temp != NULL){
                            *(p_buffer++) = *(p_temp++);
                            counter++;
                        }
                        break;

                    default:
                        break;

                }
            break;

            default:
                *(p_buffer++) = *(p_string++);
                counter++;
        }
    }

    va_end(arg);
    p_buffer = NULL;
    puts(buffer);

    return counter;
}
