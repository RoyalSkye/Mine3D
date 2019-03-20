#ifndef QUICREATOR_H
#define QUICREATOR_H

#include <QMainWindow>

namespace Ui
{
class QUICreator;
}

class QUICreator : public QMainWindow
{
    Q_OBJECT

public:
    explicit QUICreator(QWidget *parent = 0);
    ~QUICreator();

private:
    Ui::QUICreator *ui;

private slots:
    void initForm();
    void initTableWidget();
    void initTreeWidget();
    void initListWidget();
    void initOther();
    void initStyle();
    void initTranslator();
    void initTreeWidget_2();
    void initListWidget_2();
    void on_importFile_clicked();
    void on_training_clicked();
};

#endif // QUICREATOR_H
